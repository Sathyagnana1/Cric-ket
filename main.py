import pandas as pd
import numpy as np
import streamlit as st

import mysql.connector
from sqlalchemy import create_engine
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
class main2:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sathya123#",
        database="cricket"
    )
    mycursor = mydb.cursor()
    mycursor = mydb.cursor(buffered=True)
    my_conn = create_engine("mysql+mysqldb://root:sathya123#@localhost:3306/cricket")

    match = pd.read_sql_query("select * from matches", con=my_conn)
    delivery = pd.read_sql_query("select * from deliveries", con=my_conn)
    total_score = pd.read_sql_query('''SELECT match_id,inning,sum(total_runs)
                                    FROM deliveries
                                    GROUP BY inning,match_id''', con=my_conn)
    total_score = total_score[total_score['inning'] == 1]
    sql = '''CREATE VIEW final AS SELECT match_id,inning,sum(total_runs)
                          FROM deliveries
                          WHERE inning=1
                          GROUP BY inning,match_id '''
    #mycursor.execute(sql)
    teams = [
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals',
        'Lucknow Supergiants',
        'Gujurat Titans'
    ]

    match['team1'] = match['team1'].str.replace('Delhi Daredevils', 'Delhi Capitals')
    match['team2'] = match['team2'].str.replace('Delhi Daredevils', 'Delhi Capitals')

    match['team1'] = match['team1'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')
    match['team2'] = match['team2'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')

    match['team1'] = match['team1'].str.replace('Rising Pune Supergiants', 'Lucknow Supergiants')
    match['team2'] = match['team2'].str.replace('Rising Pune Supergiants', 'Lucknow Supergiants')

    match['team1'] = match['team1'].str.replace('Kochi Tuskers Kerala', 'Gujurat Titans')
    match['team2'] = match['team2'].str.replace('Kochi Tuskers Kerala', 'Gujurat Titans')

    match['team1'] = match['team1'].str.replace('Kings XI Punjab', 'Punjab KIngs')
    match['team2'] = match['team2'].str.replace('Kings XI Punjab', 'Punjab KIngs')

    match = match[match['team1'].isin(teams)]
    match = match[match['team2'].isin(teams)]

    sql = "UPDATE matches SET team1 = 'Punjab Kings' WHERE team1 = 'Kings XI Punjab'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET toss_winner = 'Punjab Kings' WHERE toss_winner = 'Kings XI Punjab'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team2 = 'Punjab Kings' WHERE team2 = 'Kings XI Punjab'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team1 = 'Delhi Capitals' WHERE team1 = 'Delhi Daredevils'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team1 = 'Sunrisers Hyderbad' WHERE team1 = 'Deccan Chargers'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team1 = 'Lucknow Supergiants' WHERE team1 = 'Rising Pune Supergiants'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team1 = 'Gujurat Titans' WHERE team1 = 'Kochi Tuskers Kerala'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team2 = 'Delhi Capitals' WHERE team2 = 'Delhi Daredevils'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team2 = 'Sunrisers Hyderbad' WHERE team2 = 'Deccan Chargers'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team2 = 'Lucknow Supergiants' WHERE team2 = 'Rising Pune Supergiants'"
    mycursor.execute(sql)
    sql = "UPDATE matches SET team2 = 'Gujurat Titans' WHERE team2 = 'Kochi Tuskers Kerala'"
    mycursor.execute(sql)

    sql = "SELECT * FROM matches WHERE dl_applied=0"
    mycursor.execute(sql)
    match = match[match['dl_applied'] == 0]
    match = match.merge(total_score[['match_id', 'sum(total_runs)']], left_on='id', right_on='match_id')

    sql = '''CREATE VIEW final2  AS
            SELECT match_id,sum(total_runs) AS total_score,city,winner
            FROM deliveries
            LEFT JOIN matches
            ON id = match_id
            GROUP BY inning,match_id'''
    #mycursor.execute(sql)
    sathya2=pd.read_sql_query("select * from final2  ",con=my_conn)
    match = match[match['dl_applied'] == 0]
    match = match[['match_id', 'city', 'winner', 'sum(total_runs)']]
    delivery = match.merge(delivery, on='match_id')
    delivery['current_score'] = delivery.groupby('match_id').cumsum()['total_runs'] - delivery['sum(total_runs)']
    delivery['runs_left'] = delivery['sum(total_runs)'] - delivery['current_score']
    delivery['balls_left'] = 126 - (delivery['over'] * 6 + delivery['ball'])
    delivery = delivery[delivery['inning'] == 2]
    df = pd.DataFrame(delivery, columns=['current_score'])

    delivery['player_dismissed'] = delivery['player_dismissed'].fillna("0")
    delivery['player_dismissed'] = delivery['player_dismissed'].apply(lambda x: x if x == "0" else "1")
    delivery['player_dismissed'] = delivery['player_dismissed'].astype('int')
    wickets = delivery.groupby('match_id').cumsum()['player_dismissed'].values
    delivery['wickets'] = 10 - wickets
    delivery['crr'] = (delivery['current_score'] * 6) / (120 - delivery['balls_left'])
    delivery['rrr'] = (delivery['runs_left'] * 6) / delivery['balls_left']

    def result(row):
        return 1 if row['batting_team'] == row['winner'] else 0

    delivery['result'] = delivery.apply(result, axis=1)
    final_df = delivery[
        ['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 'wickets', 'sum(total_runs)', 'crr', 'rrr',
         'result']]
    final_df = final_df.sample(final_df.shape[0])
    final_df.dropna(inplace=True)
    final_df = final_df[final_df['balls_left'] != 0]

    X = final_df.iloc[:, :-1]
    y = final_df.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    trf = ColumnTransformer([
        ('trf', OneHotEncoder(sparse=False, drop='first'), ['batting_team', 'bowling_team', 'city'])
    ], remainder='passthrough')
    pipe = Pipeline(steps=[
        ('step1', trf),
        ('step2', LogisticRegression(solver='liblinear'))
    ])

    pipe.fit(X_train, y_train)

    Pipeline(steps=[('step1',
                     ColumnTransformer(remainder='passthrough',
                                       transformers=[('trf',
                                                      OneHotEncoder(drop='first',
                                                                    sparse=False),
                                                      ['batting_team',
                                                       'bowling_team', 'city'])])),
                    ('step2', LogisticRegression(solver='liblinear'))])

    y_pred = pipe.predict(X_test)
    (pipe.predict_proba(X_test)[10])

    def match_summary(row):
        print("Batting Team-" + row['batting_team'] + " | Bowling Team-" + row['bowling_team'] + " | Target- " + str(
            row['sum(total_runs)']))

    def match_progression(x_df, match_id, pipe):
        match = x_df[x_df['match_id'] == match_id]
        match = match[(match['ball'] == 6)]
        temp_df = match[
            ['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 'wickets', 'sum(total_runs)', 'crr',
             'rrr']].dropna()
        temp_df = temp_df[temp_df['balls_left'] != 0]
        result = pipe.predict_proba(temp_df)
        temp_df['lose'] = np.round(result.T[0] * 100, 1)
        temp_df['win'] = np.round(result.T[1] * 100, 1)
        temp_df['end_of_over'] = range(1, temp_df.shape[0] + 1)

        target = temp_df['sum(total_runs)'].values[0]
        runs = list(temp_df['runs_left'].values)
        new_runs = runs[:]
        runs.insert(0, target)
        temp_df['runs_after_over'] = np.array(runs)[:-1] - np.array(new_runs)
        wickets = list(temp_df['wickets'].values)
        new_wickets = wickets[:]
        new_wickets.insert(0, 10)
        wickets.append(0)
        w = np.array(wickets)
        nw = np.array(new_wickets)
        temp_df['wickets_in_over'] = (nw - w)[0:temp_df.shape[0]]

        print("Target-", target)
        temp_df = temp_df[['end_of_over', 'runs_after_over', 'wickets_in_over', 'lose', 'win']]
        return temp_df, target
    def answer(inpu):

        result = main2.pipe.predict_proba((inpu))
        loss = result[0][0]
        win = result[0][1]
        batting_team = "- " + str(round(win * 100))
        bowling_team = "- " + str(round(loss * 100))

    # input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'balls_left':[balls_left],'wickets':[wickets],'sum(total_runs)':[target],'crr':[crr],'rrr':[rrr]})
    temp_df, target = match_progression(delivery, 74, pipe)
    mydb.commit()

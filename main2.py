import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import mysql.connector
from sqlalchemy import create_engine
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error

class main1:

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
    delivery=pd.read_sql_query("select * from deliveries where inning=1",con=my_conn)
    delivery=delivery.drop(['inning','non_striker','is_super_over','wide_runs', 'bye_runs','legbye_runs', 'noball_runs', 'penalty_runs', 'batsman_runs','extra_runs', 'dismissal_kind', 'fielder'],axis=1)
    delivery['balls'] = ((delivery['over'] -1) * 6 + delivery['ball'])

    match=pd.read_sql_query("select city , id from matches where dl_applied=0",con=my_conn)
    delivery = pd.merge(delivery, match, how='inner', left_on = 'match_id', right_on = 'id')


    delivery=delivery.drop(['id'],axis=1)
    sql="SELECT * FROM  deliveries WHERE ball<=6"
    mycursor.execute(sql)
    delivery=delivery[delivery['balls']<=120]


    sql = '''CREATE VIEW final3 AS SELECT match_id,inning,sum(total_runs)
                              FROM deliveries
                              WHERE inning=1
                              GROUP BY inning,match_id '''

    total= delivery.groupby('match_id').sum()['total_runs'].reset_index()
    delivery = delivery.merge(total, on='match_id')
    delivery['balls_left'] = 120 - delivery['balls']
    delivery.drop(columns=['balls'], inplace=True)
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

    delivery['batting_team'] = delivery['batting_team'].str.replace('Kings XI Punjab', 'Punjab Kings')
    delivery['batting_team'] = delivery['batting_team'].str.replace('Kings XI Punjab', 'Punjab Kings')
    delivery['batting_team'] = delivery['batting_team'].str.replace('Delhi Daredevils', 'Delhi Capitals')
    delivery['bowling)_team'] = delivery['bowling_team'].str.replace('Delhi Daredevils', 'Delhi Capitals')
    delivery['batting_team'] = delivery['batting_team'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')
    delivery['bowling)_team'] = delivery['bowling_team'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')
    delivery['batting_team'] = delivery['batting_team'].str.replace('Rising Pune Supergiants', 'Lucknow Supergiants')
    delivery['bowling)_team'] = delivery['bowling_team'].str.replace('Rising Pune Supergiants', 'Lucknow Supergiants')
    delivery['batting_team'] =  delivery['batting_team'].str.replace('Kochi Tuskers Kerala', 'Gujurat Titans')
    delivery['bowling)_team'] = delivery['bowling_team'].str.replace('Kochi Tuskers Kerala', 'Gujurat Titans')

    delivery = delivery[delivery['bowling_team'].isin(teams)]
    delivery = delivery[delivery['batting_team'].isin(teams)]

    groups = delivery.groupby('match_id')
    sql="select distinct id from matches"
    mycursor.execute(sql)

    match_ids = delivery['match_id'].unique()
    delivery.dropna(inplace=True)
    delivery = (delivery.drop(['bowling)_team'], axis=1))
    print(delivery[['over','ball']])

    delivery['current_score'] = delivery.groupby('match_id').cumsum()['total_runs_x']
    delivery['balls_bowled'] = (delivery['over'].astype('int') * 6) + delivery['ball'].astype('int')
    delivery['crr'] = round((delivery['current_score'] * 6) / delivery['balls_bowled'], 2)
    delivery['player_dismissed'] = delivery['player_dismissed'].apply(lambda x: 0 if x == '0' else 1)
    delivery['player_dismissed'] = delivery['player_dismissed'].astype('int')
    delivery['player_dismissed'] = delivery.groupby('match_id').cumsum()['player_dismissed']
    delivery['wickets_left'] = 10 - delivery['player_dismissed']

    groups =delivery.groupby('match_id')
    match_ids = delivery['match_id'].unique()
    last_five = []
    for id in match_ids:
        last_five.extend(groups.get_group(id).rolling(window=30).sum()['total_runs_x'].values.tolist())
    delivery['last_five'] = last_five

    print(delivery.columns)

    X = delivery[['batting_team','bowling_team','city', 'current_score','balls_left', 'wickets_left', 'crr', 'last_five']]
    y = delivery['total_runs_y']
    print(X.columns)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    trf = ColumnTransformer([
        ('trf', OneHotEncoder(sparse=False, drop='first'), ['batting_team', 'bowling_team', 'city'])], remainder='passthrough')
    pipe = Pipeline(steps=[
        ('step1', trf),
        ('step2', StandardScaler()),
        ('step3', XGBRegressor(n_estimators=1000, learning_rate=0.2, max_depth=12, random_state=1)) ])
    pipe.fit(X_train,y_train)
    y_pred = pipe.predict(X_test)
    print(r2_score(y_test, y_pred))
    print(mean_absolute_error(y_test, y_pred))


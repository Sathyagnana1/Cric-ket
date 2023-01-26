import plotly
import altair as alt
import seaborn as sns
import math
import pandas as pd
import random
import mysql.connector
from sqlalchemy import create_engine
import main4
import time
import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sathya123#",
    database="cricket"
)
mycursor = mydb.cursor(buffered=True)
my_conn = create_engine("mysql+mysqldb://root:sathya123#@localhost:3306/cricket")

def winpredictor():

    hide_decoration_bar_style = '''
                       <style>
                           header {visibility: hidden;}
                       </style>
                   '''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
    st.markdown(
        "<h1 style='text-align: left; color: black; position:relative; top:-100px; left:-100px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> IPL Statistics </h1>",
        unsafe_allow_html=True)




def add_bg_from_url():
    st.markdown(
        f"""
                       <style>
                       .stApp {{
                           background-image: url("https://wallpaperaccess.com/full/3819182.jpg");
                           background-attachment: fixed;
                           background-repeat: no-repeat;
                           background-position: center;
                            background-size: 1546px 750px;
                           }}
                       </style>
                       """,
        unsafe_allow_html=True
    )


add_bg_from_url()
winpredictor()
def dynamic():
    lis = ["https://www.deccanherald.com/sites/dh/files/gallery_images/2022/05/30/IPL.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/Gujarat%20Titans%20IPL%202022_2.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/Chennai%20Super%20Kings%20IPL%202021.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/Mumbai%20Indians%20IPL%202020.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/CSK%20IPL%202018.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/MI%20IPL%202017.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/SRH%20IPL%202016.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/MI%20IPL%202015.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/KKR%20IPL%202014.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/MI%20IPL%202013.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/KKR%20IPL%202012.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/CSK%20IPL%202011.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/CSK%20IPL%202010.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/Deccan%20Chargers%202009.jpg",
           "https://www.deccanherald.com/sites/dh/files/styles/gallery_thumbnails/public/gallery_images/2022/05/30/Rajasthan%20Royals%202008.jpg"]



    placeholder = st.empty()
    for j in range(100):
        for i in range(len(lis)):
            placeholder.image(lis[i])
            time.sleep(3)

def Statistics():

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sathya123#",
            database="cricket"
        )
        mycursor = mydb.cursor(buffered=True)
        my_conn = create_engine("mysql+mysqldb://root:sathya123#@localhost:3306/cricket")

        lis1 = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Delhi Capitals', 'Kolkata Knight Riders',
                'Royal Challengers Bangalore', 'Chennai Super Kings', 'Rajasthan Royals']


        col1, col3= st.columns([1,1], gap="medium")
        with col1:
            st.markdown(
                f'<h2 style="background-color:black;color:white;font-size:24px;border-radius:2%;">Top Matches Stats</h2>',
                unsafe_allow_html=True)
            st.write('')
            placeholder = st.empty()
            placeholder1 = st.empty()
            placeholder2 = st.empty()
            placeholder3 = st.empty()

            placeholder.write("")
            #time.sleep(1)
            for i in range(2):
                num1 = random.randint(1, len(lis1)-1)
                print(num1)
                match = pd.read_sql_query(
                    "select season ,city,team1,team2,toss_winner,toss_decision,winner,win_by_runs,win_by_wickets,venue "
                    "from matches where team1=%s and team2=%s", con=my_conn, params=[lis1[num1], lis1[num1-1]])
                match = match.head(1)
                wins1=(lis1[num1] + " VS " + lis1[num1-1] + " at " + match.iloc[0]['venue']+" "+str(match.iloc[0]['season']))
                placeholder1.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:20px;border-radius:2%;">{wins1}</h4>',
                    unsafe_allow_html=True)
                time.sleep(1)
                wins2=(
                    match.iloc[0]['toss_winner'] + " won the toss and opted to " + match.iloc[0][
                        'toss_decision'])
                placeholder2.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:20px;border-radius:2%;">{wins2}</h4>',
                    unsafe_allow_html=True)
                time.sleep(1)
                if match.iloc[0]['win_by_runs'] == 0:
                    wins3=(match.iloc[0]['winner'] + ' won by ' + str(
                        match.iloc[0]['win_by_wickets']) + " wickets")
                    placeholder3.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:22px;border-radius:2%;">{wins3}</h4>',
                        unsafe_allow_html=True)
                    time.sleep(1)
                else:
                    wins3=(
                        match.iloc[0]['winner'] + ' won by ' + str(match.iloc[0]['win_by_runs']) + " runs")
                    placeholder3.markdown(
                        f'<h3 style="background-color:black;color:white;font-size:22px;border-radius:2%;">{wins3}</h3>',
                        unsafe_allow_html=True)
                    time.sleep(1)
        with col3:
                st.markdown(
                f'<h2 style="background-color:black;color:white;font-size:24px;border-radius:2%;">Top Matches Stats</h2>',
                unsafe_allow_html=True)
                st.write('')
                st.write('')
                placeholder = st.empty()
                placeholder1 = st.empty()
                placeholder2 = st.empty()
                placeholder3 = st.empty()
                placeholder4 = st.empty()
                average = pd.read_sql_query("SELECT Name ,Avg FROM batstats where Avg = (SELECT max(Avg)FROM batstats)",con=my_conn)
                average = average.head(1)
                dt1=("Highest average -" +average.iloc[0]['Name']+" "+str(average.iloc[0]['Avg']))
                placeholder1.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{dt1}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)
                average = pd.read_sql_query(
                "SELECT Name,SR FROM batstats where SR  = (SELECT max(SR)FROM batstats)", con=my_conn)
                average = average.head(1)
                dt2=("Highest strike rate -" + average.iloc[0]['Name'] + " " + str(average.iloc[0]['SR']))
                placeholder2.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{dt2}</h3>',
                    unsafe_allow_html=True)
                time.sleep(2)
                average = pd.read_sql_query(
                    "SELECT Name,Runs FROM batstats where Runs   = (SELECT max(Runs)FROM batstats)",
                    con=my_conn)
                average = average.head(1)
                dt3=(
                    "Highest runs -" + average.iloc[0]['Name'] + " " + str(average.iloc[0]['Runs']))
                placeholder3.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{dt3}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)
                average = pd.read_sql_query(
                    "SELECT batsman ,`out` FROM `most_runs_average_strikerate (1)` where `out`  = (SELECT max(`out`)FROM `most_runs_average_strikerate (1)`)",
                    con=my_conn)
                average = average.head(1)
                dt4 = (
                        "Highest no of dismissals -" + average.iloc[0]['batsman'] + " " + str(average.iloc[0]['out']))
                placeholder3.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:22px;border-radius:2%;">{dt4}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)
                average = pd.read_sql_query(
                    "SELECT Name ,`Maidens` FROM `alldatabowling` where `Maidens`    = (SELECT max(`Maidens`)FROM `alldatabowling`)",
                    con=my_conn)
                average = average.head(1)
                dt1=(
                    "Highest Maidens Bowled -" + average.iloc[0]['Name'] + " " + str(average.iloc[0]['Maidens']))
                placeholder1.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{dt1}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)
                average = pd.read_sql_query(
                    "SELECT Player ,Ov FROM bowlstats where Ov  = (SELECT max(Ov)FROM bowlstats)",
                con=my_conn)
                average = average.head(1)
                dt2=(
                     "Highest Overs Bowled -" + average.iloc[0]['Player'] + " " + str(average.iloc[0]['Ov']))
                placeholder2.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{dt2}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)
                average = pd.read_sql_query(
                    "SELECT Player ,Wkts FROM bowlstats where Wkts   = (SELECT max(Wkts)FROM bowlstats)",
                    con=my_conn)
                average = average.head(1)
                dt3=(
                    "Highest Wicktes Taken -" + average.iloc[0]['Player'] + " " + str(average.iloc[0]['Wkts']))
                placeholder3.markdown(
                    f'<h3 style="background-color:black;color:white;font-size:28px;border-radius:2%;">{dt3}</h3>',
                    unsafe_allow_html=True)
                time.sleep(1)

        dynamic()





def TEAMSTATISTICS():
    st.markdown(
        "<h2 style='text-align: left; color: black; position:relative; top:-120px; left:-80px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> Team Statistics </h2>",
        unsafe_allow_html=True)
    st.sidebar.markdown("Team Statistics")
    df = pd.read_sql_query("select * from `teamwise_home_and_away`",con=my_conn)
    homwwins=df['home_win_percentage'].tolist()
    awaywins=df['away_win_percentage'].tolist()
    myexplode = [0,0,0,0,0,0,0,0]
    team=df['team'].tolist()
    print(team)
    teams = ['Chennai Super Kings', 'Delhi Capitals', 'Kolkata Knight Riders', 'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
    teamenter = st.selectbox('Select the team', (teams))
    i=teams.index(teamenter)
    print(i)
    myexplode[i]=0.2
    st.write('')

    if st.button("Get Information"):
        team1="Selected Team is "+teamenter
        st.markdown(f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{team1}</h3>',
                    unsafe_allow_html=True)
        st.write('')
        fig1, ax1 = plt.subplots()
        ax1.pie(homwwins, labels=team, autopct='%1.1f%%',
                shadow=True, explode=myexplode, startangle=90)
        plt.title("Home wins")
        ax1.axis('equal')
        fig2, ax2 = plt.subplots()
        ax2.pie(awaywins, labels=team, autopct='%1.1f%%',
                shadow=True, explode=myexplode, startangle=90)
        plt.title("Away wins")
        ax1.axis('equal')
        placeholder = st.empty()
        placeholder.pyplot(fig1)
        time.sleep(3)
        placeholder.pyplot(fig2)
        time.sleep(3)
        placeholder.empty()
        data = pd.read_sql_query("select * from `teamwise_home_and_away` where team=%s", con=my_conn,
                                 params=[teamenter])
        st.write(' ')
        col3, col4, col5 = st.columns([2, 2, 2], gap="small")
        with col3:
            matches = "Home Matches Played: " + str(math.floor(data.iloc[0]['home_matches'])) + " matches"
            matches1 = "Away Matches Played: " + str(math.floor(data.iloc[0]['away_matches'])) + " matches"
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:22.5px;border-radius:2%;">{matches}</h4>',
                unsafe_allow_html=True)
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:22.5px;border-radius:2%;">{matches1}</h4>',
                unsafe_allow_html=True)
        with col4:
            wins = "Home Matches Wins: " + str(math.floor(data.iloc[0]['home_wins'])) + " matches"
            wins1 = "Away Matches Wins: " + str(math.floor(data.iloc[0]['away_wins'])) + " matches"
            st.markdown(f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{wins}</h3>',
                        unsafe_allow_html=True)
            st.markdown(
                f'<h3 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{wins1}</h3>',
                unsafe_allow_html=True)
        with col5:
            percent = "Home Matches Wins Percentage: " + str(math.floor(data.iloc[0]['home_win_percentage'])) + " %"
            percent1 = "Away Matches Wins  Percentage: " + str(math.floor(data.iloc[0]['away_win_percentage'])) + " %"
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:22.5px;border-radius:2%;">{percent}</h4>',
                unsafe_allow_html=True)
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:22.5px;border-radius:2%;">{percent1}</h4>',
                unsafe_allow_html=True)
        st.write(' ')
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig1)
        with col2:
            st.pyplot(fig2)

        st.write(' ')
        ipl_matches_df=pd.read_sql_query("select * from matches",con=my_conn)
        team_wins_ser = ipl_matches_df['winner'].value_counts()

        team_wins_df = pd.DataFrame(columns=["team", "wins"])
        for items in team_wins_ser.iteritems():
            temp_df1 = pd.DataFrame({
                'team': [items[0]],
                'wins': [items[1]]
            })
            team_wins_df = team_wins_df.append(temp_df1, ignore_index=True)
        fig1 = plt.figure(figsize=(10, 4))
        plt.title("Total Victories of IPL Teams")
        sns.barplot(x='wins', y='team', data=team_wins_df, palette='Paired')
        st.pyplot(fig1)

        teams_per_season = ipl_matches_df.groupby('Season')['winner'].value_counts()
        year = 2008
        win_per_season_df = pd.DataFrame(columns=['year', 'team', 'wins'])
        for items in teams_per_season.iteritems():
            if items[0][0] == year:
                print(items)
                win_series = pd.DataFrame({
                    'year': [items[0][0]],
                    'team': [items[0][1]],
                    'wins': [items[1]]
                })
                win_per_season_df = win_per_season_df.append(win_series)
                year += 1
        fig = plt.figure(figsize=(10, 4))
        plt.title("Wins of IPL Teams in each season")
        sns.barplot('wins', 'team', hue='year', data=win_per_season_df, palette='Paired')
        st.pyplot(fig)

def PLAYERSTATISTICS():
    st.markdown(
        "<h2 style='text-align: left; color: black; position:relative; top:-120px; left:-80px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> Player Statistics </h2>",
        unsafe_allow_html=True)
    st.sidebar.markdown("Player Statistics")
    choice=st.selectbox("Know your favourite batsman or bowler stats!!",("------","Batsman","Bowler"))
    if choice=="Batsman":
        names = pd.read_sql_query("select b.Name from batstats b,`alldatabatting` a where a.Name=b.Name", con=my_conn)
        teams = names['Name'].tolist()
        teams = list(set(teams))
        teams.sort()
        print(len(teams))
        teams.insert(0,"-----")
        teamenter = st.selectbox('Select the player', (teams))
        option=st.selectbox("Select your option",("------","Get Information","Get Detailed Comparsion","Compare your player with any player"))
        if option=="Get Information":
            bat = pd.read_sql_query("select * from batstats where Name=%s  order by Runs", con=my_conn,
                                    params=[teamenter])
            bat1 = pd.read_sql_query("select * from batstats  order by Runs desc", con=my_conn)
            ranklis = bat1['Name'].tolist()
            lis5 = (bat['Name'].tolist())
            if (bat.iloc[0]['Name'] in ranklis):
                rank = ranklis.index(bat.iloc[0]['Name'])

            txt = "Rank of " + bat.iloc[0]['Name'] + " is " + str(rank + 1)
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">{txt}<h4>',
                unsafe_allow_html=True)
            col10, col11 = st.columns(2, gap='small')
            with col10:
                txt = "Matches Played : " + str(bat.iloc[0]['Match'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            with col11:
                txt = "Innings Played : " + str(bat.iloc[0]['Inn'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            col3, col4, col5, col6 = st.columns(4, gap='small')
            with col3:
                txt = "Runs scored : " + str(bat.iloc[0]['Runs'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            with col4:
                txt1 = "Average runs: " + str(bat.iloc[0]['Avg'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">{txt1}<h4>',
                    unsafe_allow_html=True)
            with col5:
                txt2 = "Highest Score : " + str(bat.iloc[0]['HS'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">{txt2}<h4>',
                    unsafe_allow_html=True)
            with col6:
                txt3 = "Strike rate : " + str(bat.iloc[0]['SR'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:22px;border-radius:2%;">{txt3}<h4>',
                    unsafe_allow_html=True)
            col6, col7, col8, col9 = st.columns(4, gap='small')
            with col6:
                txt4 = "Fours hit : " + str(bat.iloc[0]['4s'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt4}<h4>',
                    unsafe_allow_html=True)
            with col7:
                txt5 = "Sixes hit : " + str(bat.iloc[0]['6s'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt5}<h4>',
                    unsafe_allow_html=True)
            with col8:
                txt6 = "Fifties : " + str(bat.iloc[0]['50'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt6}<h4>',
                    unsafe_allow_html=True)
            with col9:
                txt7 = "Centuries : " + str(bat.iloc[0]['100'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt7}<h4>',
                    unsafe_allow_html=True)

        if (option==("Get Detailed Comparsion")):
            data = pd.read_sql_query("select * from `alldatabatting` where Name=%s", con=my_conn, params=[teamenter])
            list1 = [data.iloc[0]['runs'], data.iloc[0]['balls']]
            list2 = ['Runs Scored', 'Dot Balls']
            fig1, ax1 = plt.subplots()
            ax1.pie(list1, labels=list2, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Runs Scored VS Dot Balls")
            ax1.axis('equal')
            list3 = [data.iloc[0]['fours'], data.iloc[0]['sixes']]
            list4 = ['Fours', 'Sixes']
            fig2, ax2 = plt.subplots()
            ax2.pie(list3, labels=list4, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Fours VS Sixes")
            ax2.axis('equal')

            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Know where your player stands<h4>',
                unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                dataog = pd.read_sql_query("select * from batstats", con=my_conn)
                data1 = pd.read_sql_query("select * from batstats order by Runs desc", con=my_conn)
                listog = dataog['Name'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿Num'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart = alt.Chart(data1).mark_bar().encode(
                    x='Name',
                    y='Runs'
                )
                st.altair_chart(bar_chart, use_container_width=True)
            with col2:
                dataog = pd.read_sql_query("select * from batstats", con=my_conn)
                data1 = pd.read_sql_query("select * from batstats order by Avg desc", con=my_conn)
                listog = dataog['Name'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿Num'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart1 = alt.Chart(data1).mark_bar().encode(
                    x='Name',
                    y='Avg'
                )
                st.altair_chart(bar_chart1, use_container_width=True)
            col3, col4 = st.columns(2)
            with col3:
                dataog = pd.read_sql_query("select * from batstats", con=my_conn)
                data1 = pd.read_sql_query("select * from batstats order by SR desc", con=my_conn)
                listog = dataog['Name'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿Num'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart2 = alt.Chart(data1).mark_bar().encode(
                    x='Name',
                    y='SR'
                )
                st.altair_chart(bar_chart2, use_container_width=True)
            with col4:
                dataog = pd.read_sql_query("select * from batstats", con=my_conn)
                data1 = pd.read_sql_query("select * from batstats order by HS desc", con=my_conn)
                listog = dataog['Name'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿Num'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart3 = alt.Chart(data1).mark_bar().encode(
                    x='Name',
                    y='HS'
                )
                st.altair_chart(bar_chart3, use_container_width=True)
            col5, col6 = st.columns(2)
            with col5:
                st.pyplot(fig1)
            with col6:
                st.pyplot(fig2)
        if (option==("Compare your player with any player")):
            names = pd.read_sql_query("select b.Name from batstats b,`alldatabatting` a where a.Name=b.Name",
                                      con=my_conn)
            teams1= names['Name'].tolist()
            teams1= list(set(teams))
            teams1.remove(teamenter)
            teams1.sort()
            print(len(teams))
            playerenter = st.selectbox('Select the player', (teams1))
            if st.button("Get information"):
                txt='     '+teamenter+' VS '+playerenter
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
                data1=pd.read_sql_query("select * from batstats where Name=%s ",con=my_conn,params=[teamenter])
                data2 = pd.read_sql_query("select * from batstats where Name=%s ", con=my_conn,
                                          params=[playerenter])
                col1,col2=st.columns(2)
                with col1:
                    txt11="Rank: "+str(data1.iloc[0]['ï»¿Num'])
                    txt1="Matches played: "+str(data1.iloc[0]['Match'])
                    txt2="Innings played: "+str(data1.iloc[0]['Inn'])
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt11}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt1}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt2}</h4>',
                        unsafe_allow_html=True)
                with col2:
                    txt112 = "Rank: " + str(data2.iloc[0]['ï»¿Num'])
                    txt1 = "Matches played: " + str(data2.iloc[0]['Match'])
                    txt2="Innings played: " + str(data2.iloc[0]['Inn'])
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt112}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt1}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt2}</h4>',
                        unsafe_allow_html=True)
                st.write('')
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Here\'s is the comparsion</h4>',
                    unsafe_allow_html=True)
                st.write('')
                df =pd.read_sql_query("select * from batstats",con=my_conn)
                rnk1=data1.iloc[0]['ï»¿Num']
                rnk2=data2.iloc[0]['ï»¿Num']
                df=df.loc[df['ï»¿Num'].isin([rnk1,rnk2])]
                col1,col2=st.columns(2,gap="small")
                with col1:
                    fig = px.bar(df, x="Name", y="Runs", height=400,width=350)
                    st.plotly_chart(fig)
                with col2:
                    fig = px.bar(df, x="Name", y=["Avg", "SR"], barmode='group', height=400,width=350)
                    st.plotly_chart(fig)
                col3,col4=st.columns(2)
                with col3:
                    fig = px.bar(df, x="Name", y=["4s", "6s"], barmode='group', height=400,width=350)
                    st.plotly_chart(fig)
                with col4:
                    df = df.loc[df['ï»¿Num'].isin([rnk1, rnk2])]
                    fig = px.bar(df, x="Name", y=["50", "100"], barmode='group', height=400,width=350)
                    # st.dataframe(df) # if need to display dataframe
                    st.plotly_chart(fig)
    if choice=="Bowler":
        names = pd.read_sql_query("select b.Player from bowlstats b,`alldatabowling` a where a.Name=b.Player", con=my_conn)
        teams = names['Player'].tolist()
        teams = list(set(teams))
        teams.sort()
        print(len(teams))
        teams.insert(0, "-----")
        teamenter = st.selectbox('Select the player', (teams))
        option = st.selectbox("Select your option", (
        "------", "Get Information", "Get Detailed Comparsion", "Compare your player with any player"))
        if option == "Get Information":
            bat = pd.read_sql_query("select * from bowlstats where Player=%s  order by Wkts", con=my_conn,
                                    params=[teamenter])
            bat1 = pd.read_sql_query("select * from bowlstats  order by Wkts desc", con=my_conn)
            ranklis = bat1['Player'].tolist()
            lis5 = (bat['Player'].tolist())
            if (bat.iloc[0]['Player'] in ranklis):
                rank = ranklis.index(bat.iloc[0]['Player'])

            txt = "Rank of " + bat.iloc[0]['Player'] + " is " + str(rank + 1)
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">{txt}<h4>',
                unsafe_allow_html=True)
            col10, col11 = st.columns(2, gap='small')
            with col10:
                txt = "Matches Played : " + str(bat.iloc[0]['Mat'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            with col11:
                txt = "Innings Played : " + str(bat.iloc[0]['Inns'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            col3, col4, col5, col6 = st.columns(4, gap='small')
            with col3:
                txt = "Overs bowled : " + str(bat.iloc[0]['Ov'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24.5px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
            with col4:
                txt1 = "Wickets taken:" + str(bat.iloc[0]['Wkts'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:25px;border-radius:2%;">{txt1}<h4>',
                    unsafe_allow_html=True)
            with col5:
                txt2 = "Runs conceded : " + str(bat.iloc[0]['Runs'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:24px;border-radius:2%;">{txt2}<h4>',
                    unsafe_allow_html=True)
            with col6:
                txt3 = "Average : " + str(bat.iloc[0]['Avg'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:25.7px;border-radius:2%;">{txt3}<h4>',
                    unsafe_allow_html=True)
            col6, col7, col8, col9 = st.columns(4, gap='small')
            with col6:
                txt4 = "Economy : " + str(bat.iloc[0]['Econ'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt4}<h4>',
                    unsafe_allow_html=True)
            with col7:
                txt5 = "Strike rate : " + str(bat.iloc[0]['SR'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt5}<h4>',
                    unsafe_allow_html=True)
            with col8:
                txt6 = " 4 Wkt Haul: " + str(bat.iloc[0]['4w'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt6}<h4>',
                    unsafe_allow_html=True)
            with col9:
                txt7 = " 5 Wkt Haul: " + str(bat.iloc[0]['5w'])
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt7}<h4>',
                    unsafe_allow_html=True)

        if (option == ("Get Detailed Comparsion")):
            data = pd.read_sql_query("select * from `alldatabowling` where Name=%s", con=my_conn, params=[teamenter])
            list1 = [math.ceil(data.iloc[0]['Over'])*6-data.iloc[0]['Dots'], data.iloc[0]['Dots']]
            list2 = ['Balls were runs scored', 'Dot Balls']
            fig1, ax1 = plt.subplots()
            ax1.pie(list1, labels=list2, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Balls were runs scored VS Dot Balls")
            ax1.axis('equal')
            list3 = [math.ceil(data.iloc[0]['Over'])*6, data.iloc[0]['Runs_Conceded']]
            list4 = ['Bowls bowled', 'Runs conceded']
            fig2, ax2 = plt.subplots()
            ax2.pie(list3, labels=list4, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Overs VS Runs conceded")
            ax2.axis('equal')

            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Know where your player stands<h4>',
                unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                dataog = pd.read_sql_query("select * from bowlstats", con=my_conn)
                data1 = pd.read_sql_query("select * from bowlstats order by Wkts", con=my_conn)
                listog = dataog['Player'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿POS'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart = alt.Chart(data1).mark_bar().encode(
                    x='Player',
                    y='Wkts'
                )
                st.altair_chart(bar_chart, use_container_width=True)
            with col2:
                dataog = pd.read_sql_query("select * from bowlstats", con=my_conn)
                data1 = pd.read_sql_query("select * from bowlstats order by Econ ASC", con=my_conn)
                listog = dataog['Player'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿POS'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart1 = alt.Chart(data1).mark_bar().encode(
                    x='Player',
                    y='Econ'
                )
                st.altair_chart(bar_chart1, use_container_width=True)
            col3, col4 = st.columns(2)
            with col3:
                dataog = pd.read_sql_query("select * from bowlstats", con=my_conn)
                data1 = pd.read_sql_query("select * from bowlstats order by Avg desc", con=my_conn)
                listog = dataog['Player'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿POS'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart2 = alt.Chart(data1).mark_bar().encode(
                    x='Player',
                    y='Avg'
                )
                st.altair_chart(bar_chart2, use_container_width=True)
            with col4:
                dataog = pd.read_sql_query("select * from bowlstats", con=my_conn)
                data1 = pd.read_sql_query("select * from bowlstats order by SR desc", con=my_conn)
                listog = dataog['Player'].tolist()
                if teamenter in listog:
                    i = listog.index(teamenter)
                if i > 3:
                    data1 = data1.loc[data1['ï»¿POS'].isin([i - 2, i - 1, i, i + 1, i + 2])]
                else:
                    data1 = data1.head(5)
                bar_chart3 = alt.Chart(data1).mark_bar().encode(
                    x='Player',
                    y='SR'
                )
                st.altair_chart(bar_chart3, use_container_width=True)
            col5, col6 = st.columns(2)
            with col5:
                st.pyplot(fig1)
            with col6:
                st.pyplot(fig2)
        if (option == ("Compare your player with any player")):
            names = pd.read_sql_query("select b.Player from bowlstats b,`alldatabowling` a where a.Name=b.Player", con=my_conn)
            teams1 = names['Player'].tolist()
            teams1 = list(set(teams))
            teams1.remove(teamenter)
            teams1.sort()
            print(len(teams))
            playerenter = st.selectbox('Select the player', (teams1))
            if st.button("Get information"):
                txt = '     ' + teamenter + ' VS ' + playerenter
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}<h4>',
                    unsafe_allow_html=True)
                data1 = pd.read_sql_query("select * from bowlstats where Player=%s ", con=my_conn, params=[teamenter])
                data2 = pd.read_sql_query("select * from bowlstats where Player=%s ", con=my_conn,
                                          params=[playerenter])
                col1, col2 = st.columns(2)
                with col1:
                    txt11 = "Rank: " + str(data1.iloc[0]['ï»¿POS'])
                    txt1 = "Matches played: " + str(data1.iloc[0]['Mat'])
                    txt2 = "Innings played: " + str(data1.iloc[0]['Inns'])
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt11}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt1}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt2}</h4>',
                        unsafe_allow_html=True)
                with col2:
                    txt112 = "Rank: " + str(data2.iloc[0]['ï»¿POS'])
                    txt1 = "Matches played: " + str(data2.iloc[0]['Mat'])
                    txt2 = "Innings played: " + str(data2.iloc[0]['Inns'])
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt112}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt1}</h4>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt2}</h4>',
                        unsafe_allow_html=True)
                st.write('')
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Here\'s is the comparsion</h4>',
                    unsafe_allow_html=True)
                st.write('')
                df = pd.read_sql_query("select * from bowlstats", con=my_conn)
                rnk1 = data1.iloc[0]['ï»¿POS']
                rnk2 = data2.iloc[0]['ï»¿POS']
                df = df.loc[df['ï»¿POS'].isin([rnk1, rnk2])]
                col1, col2 = st.columns(2, gap="small")
                with col1:
                    fig = px.bar(df, x="Player", y="Ov", height=400, width=350)
                    st.plotly_chart(fig)
                with col2:
                    fig = px.bar(df, x="Player", y=["Wkts", "Econ"], barmode='group', height=400, width=350)
                    st.plotly_chart(fig)
                col3, col4 = st.columns(2)
                with col3:
                    fig = px.bar(df, x="Player", y=["Avg", "SR"], barmode='group', height=400, width=350)
                    st.plotly_chart(fig)
                with col4:
                    df = df.loc[df['ï»¿POS'].isin([rnk1, rnk2])]
                    fig = px.bar(df, x="Player", y=["4w", "5w"], barmode='group', height=400, width=350)
                    st.plotly_chart(fig)

def MATCHSTATISTICS():
    st.markdown(
        "<h2 style='text-align: left; color: black; position:relative; top:-120px; left:-80px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> Match Statistics </h2>",
        unsafe_allow_html=True)
    st.sidebar.markdown("Match Statistics")
    st.markdown(
        "<h4 style='text-align: left; color: black; position:relative; top:-120px; left:60px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> Know the details of your Favourite match </h4>",
        unsafe_allow_html=True)
    teams = [
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Punjab Kings',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals',
    ]
    teams.insert(0, "-----")
    col1, col2, col3 = st.columns(3)
    with col1:
        teamenter1 = st.selectbox('Select the host team', sorted(teams))
    teams.remove(teamenter1)
    with col2:
        bowling_team = st.selectbox('Select the visting team', sorted(teams))
    option = st.selectbox("Select your option", ("--------", "Get match overview", "Get detailed information","Analayse the match"))
    with col3:
        season = st.selectbox("Select the season", (
        '2008', '2009', '2010', '2012', '2011', '2013', '2014', '2015', '2016', '2017', '2018', '2019'))
    if option=="Get match overview":
        matches=pd.read_sql_query("select * from matches where team1=%s and team2=%s and season=%s",con=my_conn,params=[teamenter1,bowling_team,season])
        st.write(' ')
        if matches.empty:
            st.error("Please check your entry and retry")
        else:
            txt = "Match : " + matches.iloc[0]['team1'] + " VS " + matches.iloc[0]['team2']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            txt = "Venue : " + matches.iloc[0]['venue'] + "," + matches.iloc[0]['city']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            txt = "Date : " + matches.iloc[0]['date']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            txt = matches.iloc[0]['toss_winner'] + " won the toss and opted to " + matches.iloc[0]['toss_decision']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            if matches.iloc[0]['win_by_wickets'] == 0:
                txt = matches.iloc[0]['winner'] + " won by " + str(matches.iloc[0]['win_by_runs']) + " runs"
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                    unsafe_allow_html=True)
            else:
                txt = matches.iloc[0]['winner'] + " won by " + str(matches.iloc[0]['win_by_wickets']) + " wickets"
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                    unsafe_allow_html=True)
            txt = "Player of the match: " + str(matches.iloc[0]['player_of_match'])
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
    if option=="Get detailed information":
        matches = pd.read_sql_query("select * from cricket.deliveries,cricket.matches where matches.team1=%s and matches.team2=%s "
                                    "and matches.Season=%s and matches.id=deliveries.match_id", con=my_conn,
                                    params=[teamenter1, bowling_team, season])
        if matches.empty:
            st.error("Empty datset")
        else:
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Scorecard</h4>',
                unsafe_allow_html=True)
            st.write('')
            txt=matches.iloc[0]['batting_team']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)

            col1,col2,col3,col4=st.columns([2,2,4,1],gap='small')
            with col1:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Batsman</h4>',
                    unsafe_allow_html=True)
            with col2:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Bowler</h4>',
                    unsafe_allow_html=True)
            with col3:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Dismissal</h4>',
                    unsafe_allow_html=True)
            with col4:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Runs</h4>',
                    unsafe_allow_html=True)
            scorecard=pd.read_sql_query("select sum(batsman_runs), sum(total_runs), batsman from cricket.deliveries  where match_id = %s and inning = 1 "
                                        "group by match_id, inning, batsman",con=my_conn,params=[matches.iloc[0]['id']])
            scorecard1=pd.read_sql_query("select bowler,ball,`over`,player_dismissed,dismissal_kind,fielder from cricket.deliveries "
                                         "where player_dismissed!='0' and match_id=%s and inning=1",con=my_conn,params=[matches.iloc[0]['id']])
            scorecard2 = pd.read_sql_query(
                "select * from cricket.deliveries  where match_id = %s and inning = 1", con=my_conn,
                params=[matches.iloc[0]['id']])
            scorecard2 = scorecard2.tail(10)
            lastover = scorecard2['over'].tolist()
            batsman=scorecard['batsman'].tolist()
            batsmanruns=scorecard['sum(batsman_runs)'].tolist()
            dismissal_kind=scorecard1['dismissal_kind'].tolist()
            fielder=scorecard1['fielder'].tolist()
            over=scorecard1['over'].tolist()
            ball=scorecard1['ball'].tolist()
            bowler=scorecard1['bowler'].tolist()
            runs=scorecard['sum(total_runs)'].tolist()
            i=0
            j=0
            while i<len(scorecard) or j<len(scorecard1):
                with col1:
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{batsman[i]}</h4>',
                        unsafe_allow_html=True)
                with col2:
                    if j>=len(scorecard1):
                        st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">---</h4>',
                        unsafe_allow_html = True)
                    else:
                        st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{bowler[i]}</h4>',
                        unsafe_allow_html=True)
                with col3:
                    if j>=len(scorecard1):
                        st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">---</h4>',
                        unsafe_allow_html = True)
                    else:
                        if dismissal_kind[i] == "bowled" or dismissal_kind[i] == "lbw":
                            txt = dismissal_kind[i] + " at " + str(over[i]) + "th over " + " by " + bowler[i]
                        else:
                            txt = dismissal_kind[i] + " at " + str(over[i]) + "th over" + " by " + fielder[i]
                        st.markdown(
                            f'<h4 style="background-color:black;color:white;font-size:19px;border-radius:2%;">{txt}</h4>',
                            unsafe_allow_html=True)
                with col4:
                    txt=str(int(batsmanruns[i]))
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                        unsafe_allow_html=True)

                i+=1
                j+=1
            txt = "Runs scored : "+str(int(sum(runs)))+"runs for "+str(len(scorecard1))+" wickets"+" at "+str(lastover[len(lastover)-1])+"th over"
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            st.title('')




            txt = matches.iloc[0]['bowling_team']
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns([2, 2, 4, 1], gap='small')
            with col1:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Batsman</h4>',
                    unsafe_allow_html=True)
            with col2:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Bowler</h4>',
                    unsafe_allow_html=True)
            with col3:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Dismissal</h4>',
                    unsafe_allow_html=True)
            with col4:
                st.markdown(
                    f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">Runs</h4>',
                    unsafe_allow_html=True)
            scorecard2= pd.read_sql_query(
                "select * from cricket.deliveries  where match_id = %s and inning = 2", con=my_conn, params=[matches.iloc[0]['id']])
            scorecard2=scorecard2.tail(10)
            lastover=scorecard2['over'].tolist()
            scorecard = pd.read_sql_query(
                "select sum(batsman_runs), sum(total_runs), batsman from cricket.deliveries  where match_id = %s and inning = 2 "
                "group by match_id, inning, batsman", con=my_conn, params=[matches.iloc[0]['id']])
            scorecard1 = pd.read_sql_query(
                "select bowler,ball,`over`,player_dismissed,dismissal_kind,fielder from cricket.deliveries "
                "where player_dismissed!='0' and match_id=%s and inning=2", con=my_conn, params=[matches.iloc[0]['id']])
            batsman = scorecard['batsman'].tolist()
            batsmanruns = scorecard['sum(batsman_runs)'].tolist()
            dismissal_kind = scorecard1['dismissal_kind'].tolist()
            fielder = scorecard1['fielder'].tolist()
            over = scorecard1['over'].tolist()
            ball = scorecard1['ball'].tolist()
            bowler = scorecard1['bowler'].tolist()
            runs = scorecard['sum(total_runs)'].tolist()

            i = 0
            j = 0
            while i < len(scorecard) or j < len(scorecard1):
                with col1:
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{batsman[i]}</h4>',
                        unsafe_allow_html=True)
                with col2:
                    if j >= len(scorecard1):
                        st.markdown(
                            f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">---</h4>',
                            unsafe_allow_html=True)
                    else:
                        st.markdown(
                            f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{bowler[i]}</h4>',
                            unsafe_allow_html=True)
                with col3:
                    if j >= len(scorecard1):
                        st.markdown(
                            f'<h4 style="background-color:black;color:white;font-size:23px;border-radius:2%;">---</h4>',
                            unsafe_allow_html=True)
                    else:
                        if dismissal_kind[i]=="bowled" or dismissal_kind[i]=="lbw":

                            txt = dismissal_kind[i] + " at " + str(over[i]) + "th over "  + " by " + bowler[i]
                        else:
                            txt = dismissal_kind[i] + " at " + str(over[i]) + "th over"  + " by " +fielder[i]
                        st.markdown(
                            f'<h4 style="background-color:black;color:white;font-size:19px;border-radius:2%;">{txt}</h4>',
                            unsafe_allow_html=True)
                with col4:
                    txt = str(int(batsmanruns[i]))
                    st.markdown(
                        f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                        unsafe_allow_html=True)

                i += 1
                j += 1
            txt = "Runs scored : " + str(int(sum(runs))) + "runs for " + str(len(scorecard1)) + " wickets"+" at "+str(lastover[len(lastover)-1])+"th over"
            st.markdown(
                f'<h4 style="background-color:black;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                unsafe_allow_html=True)
            st.title('')
            mat=pd.read_sql_query("select * from matches where team1=%s and team2=%s and season=%s",con=my_conn,params=[teamenter1,bowling_team,season])
            if mat.iloc[0]['win_by_wickets'] == 0:
                txt = mat.iloc[0]['winner'] + " won by " + str(mat.iloc[0]['win_by_runs']) + " runs"
                st.markdown(
                    f'<h4 style="background-color:green;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                    unsafe_allow_html=True)
            else:
                txt = mat.iloc[0]['winner'] + " won by " + str(mat.iloc[0]['win_by_wickets']) + " wickets"
                st.markdown(
                    f'<h4 style="background-color:green;color:white;font-size:21px;border-radius:2%;">{txt}</h4>',
                    unsafe_allow_html=True)
    if option=="Analayse the match":
        matches = pd.read_sql_query(
            "select * from cricket.deliveries,cricket.matches where matches.team1=%s and matches.team2=%s "
            "and matches.Season=%s and matches.id=deliveries.match_id", con=my_conn,
            params=[teamenter1, bowling_team, season])
        runs_overs = []
        for i in range(1, 21):
            delivery = pd.read_sql_query(
                "select sum(total_runs) from deliveries where match_id=%s and inning=1 and `over`=%s ", params=[matches.iloc[0]['match_id'],str(i)],
                con=my_conn)
            runs_overs.append(delivery.iloc[0]['sum(total_runs)'])
        runs_overs1 = []
        for i in range(1, 21):
            delivery = pd.read_sql_query(
                "select sum(total_runs) from deliveries where match_id=%s and inning=2 and `over`=%s ",
                params=[matches.iloc[0]['match_id'], str(i)],
                con=my_conn)
            runs_overs1.append(delivery.iloc[0]['sum(total_runs)'])
        overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        data = {'overs': overs, 'runs by 1st team': runs_overs,'runs by 2nd team':runs_overs1}
        df = pd.DataFrame(data)
        fig = px.bar(df, x="overs", y=["runs by 1st team", "runs by 2nd team"], barmode='group', height=400, width=700,title='Over by over comparsion')
        st.plotly_chart(fig)
        scorecard = pd.read_sql_query(
            "select sum(batsman_runs), sum(total_runs), batsman from cricket.deliveries  where match_id = %s and inning = 2 "
            "group by match_id, inning, batsman", con=my_conn, params=[matches.iloc[0]['id']])
        res= [sum(runs_overs[ : i + 1]) for i in range(len(runs_overs))]
        for i in range(len(runs_overs1)):
             if runs_overs1[i] ==None:
                runs_overs1[i] = runs_overs1[i-1]

        res1 = [sum(runs_overs1[: i + 1]) for i in range(len(runs_overs1))]
        data = {'overs': overs, '1st innings': res, '2nd innings': res1}
        df = pd.DataFrame(data)
        fig1 = px.line(df, x="overs", y=["1st innings","2nd innings"], height=400, width=700, title='Match Progression')
        st.plotly_chart(fig1)
        col1,col2=st.columns(2)
        with col1:
            df1 = pd.read_sql_query(
                "select sum(batsman_runs), sum(total_runs), batsman ,sum(ball) from cricket.deliveries  "
                "where match_id = %s and inning = 1 group by match_id, inning, batsman", con=my_conn,
                params=[matches.iloc[0]['id']])
            batsmanruns = df1['sum(batsman_runs)'].tolist()
            batsman = df1['batsman'].tolist()
            fig3, ax3 = plt.subplots()
            ax3.pie(batsmanruns, labels=batsman, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Scores 1St innings")
            ax3.axis('equal')
            st.pyplot(fig3)
        with col2:
            df1 = pd.read_sql_query(
                "select sum(batsman_runs), sum(total_runs), batsman ,sum(ball) from cricket.deliveries  "
                "where match_id = %s and inning = 2 group by match_id, inning, batsman", con=my_conn,
                params=[matches.iloc[0]['id']])
            batsmanruns = df1['sum(batsman_runs)'].tolist()
            batsman = df1['batsman'].tolist()
            fig4, ax4 = plt.subplots()
            ax4.pie(batsmanruns, labels=batsman, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.title("Scores 2nd innings")
            ax4.axis('equal')
            st.pyplot(fig4)

page_names_to_funcs = {
    "Statistics":Statistics,
    "Team Statistics": TEAMSTATISTICS,
    "Player Statistics": PLAYERSTATISTICS,
    "Match Statistics": MATCHSTATISTICS,
}

selected_page = st.sidebar.selectbox("Select your option", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
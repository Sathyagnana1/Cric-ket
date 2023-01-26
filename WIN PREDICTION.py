import streamlit as st
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

import cric_ket
import main

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
        "<h1 style='text-align: left; color: black; position:relative; top:-100px; left:-30px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> IPL Win Predictor</h1>",
        unsafe_allow_html=True)



def add_bg_from_url():
    st.markdown(
        f"""
                       <style>
                       .stApp {{
                           background-image: url("https://wallpaperaccess.com/full/3819159.jpg");
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
teams = ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore','Kolkata Knight Riders','Kings XI Punjab','Chennai Super Kings','Rajasthan Royals','Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi','Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth','Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley','Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala','Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi','Sharjah', 'Mohali', 'Bengaluru']
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))
target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left= target - score
    balls_left = 120 - (overs*6)
    wickets = 10-wickets
    crr = score/overs
    rrr = (runs_left)/(20-overs)
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
                         'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'sum(total_runs)':[target],'crr':[crr],'rrr':[rrr]})
    result = main.main2.pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    col1, col2 = st.columns(2)
    with col3:
        st.success(batting_team + "- " + str(round(win * 100)) + "%")
    with col4:
        st.error((bowling_team + "- " + str(round(loss*100)) + "%"))


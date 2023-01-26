import streamlit as st
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import main2

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
        "<h1 style='text-align: left; color: black; position:relative; top:-100px; left:-30px; margin-left:0px; margin-right:0px;font-family:Britannic Bold; text-size:50px'> IPL Score Predictor</h1>",
        unsafe_allow_html=True)



def add_bg_from_url():
    st.markdown(
        f"""
                       <style>
                       .stApp {{
                           background-image: url("https://wallpaperaccess.com/full/3819161.jpg");
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

teams = ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore','Kolkata Knight Riders','Punjab Kings','Chennai Super Kings','Rajasthan Royals','Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi','Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth','Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley','Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala','Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi','Sharjah', 'Mohali', 'Bengaluru']


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')
last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs
    balls_bowled=(overs*6)
    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
         'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr], 'last_five': [last_five]})
    result = main2.main1.pipe.predict(input_df)
    st.warning("Predicted Score - " + str(int(result[0])))








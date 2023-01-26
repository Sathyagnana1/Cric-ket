import pandas as pd
import streamlit as st
import mysql.connector
from sqlalchemy import create_engine

class cric_firstpage:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sathya123#",
        database="cricket"
    )
        mycursor = mydb.cursor(buffered=True)
        my_conn = create_engine("mysql+mysqldb://root:sathya123#@localhost:3306/cricket")

        st.set_page_config(page_title="CRIC_KET", page_icon="🏏")
        hide_decoration_bar_style = '''
                           <style>
                               header {visibility: hidden;}
                           </style>
                       '''
        st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
        st.markdown(
            f"""
                                <style>
                                .stApp {{
                                            background-image: url("https://wallpapercave.com/wp/wp3049854.jpg");
                                            background-attachment: fixed;
                                            background-repeat: no-repeat;
                                            background-position: center;
                                            background-size: 1546px 750px;
                                                   }}
                                               </style>
                                               """,
            unsafe_allow_html=True
        )
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
        with col1:
            st.write(' ')
        with col2:
            st.write(' ')
        with col3:
            st.write(' ')
        with col4:
            st.write(' ')
        with col5:
            st.write(' ')
        with col6:
            st.write(' ')
        with col7:
            st.write(' ')
        with col8:
            st.write(' ')
        with col9:
            st.write(' ')
        with col10:
            st.write(' ')
            '''st.image(
                "https://o.remove.bg/downloads/69b1913b-2c2e-47cf-b093-206d7ef8aa8b/1000_F_313047846_Lo81mZoTf67UV9FkJLswz0FLMXc4Q7xc-removebg-preview.png",
                width=200)'''
        st.markdown(
            "<h1 style='text-align: left; color: white; position:relative; top:-130px; left:-110px; margin-left:0px; margin-right:0px;font-family:Proxima Nova; text-size:50px'> CRIC_KET</h1>",
            unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align: left; color: black; position:relative; top:-130px; left:-110px; margin-left:0px; margin-right:0px;font-family:Broadway; text-size:20px'> One stop solution for IPL needs</h2>",
            unsafe_allow_html=True)

        hide_bar = """
                    <style>
                    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                        visibility:hidden;
                        width: 0px;
                    }
                    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                        visibility:hidden;
                    }
                    </style>
                """
        st.markdown(hide_bar,unsafe_allow_html=True)
        choice=st.selectbox('',('Login','Signup'))
        if(choice=="Login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            if st.button("Submit"):
                mycursor.execute("SELECT * FROM user WHERE Username = %s AND Password = %s", (username, password))
                if mycursor.fetchone():
                    st.success("Logged in successfully!")

                    show_bar = """
                        <style>
                        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                            visibility:visible;
                            width: 350px;
                        }
                        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                            visibility:visible;
                        }
                        </style>
                    """
                    st.markdown(show_bar,unsafe_allow_html=True)
                else:
                    st.error("Incorrect username or password.")
        if choice=="Signup":
            name=st.text_input("Name")
            email = st.text_input("Email")
            username1 = st.text_input("Username")
            password1 = st.text_input("Password", type='password')
            confirm_password1 = st.text_input("Confirm Password", type='password')
            if st.button("Submit"):

                if password1 == confirm_password1:
                    details = pd.read_sql_query("select * from user", con=my_conn)
                    names = details['Name'].tolist()
                    usernames = details['Username'].tolist()
                    passwords = details['Password'].tolist()
                    if name in names or username1 in usernames :
                        st.error("Credentials already used")
                    else:
                        mycursor.execute("INSERT INTO user (Name,Email,Username,Password) VALUES (%s,%s, %s, %s)",
                                         (name, email, username1, password1))

                        mycursor.execute('''CREATE TRIGGER t2
                                                                   AFTER INSERT ON user
                                                                   FOR EACH ROW 
                                                                   BEGIN
                                                                   INSERT INTO userback VALUES (%s,%s, %s, %s);END;''',
                                         (name, email, username1, password1))

                        mydb.commit()
                        st.success("Account created!")


                else:
                    st.error("Passwords do not match.")
import pandas as pd
import numpy as np
import streamlit as st

import mysql.connector
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
class main3:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sathya123#",
        database="cricket"
    )
    mycursor = mydb.cursor()
    mycursor = mydb.cursor(buffered=True)
    my_conn = create_engine("mysql+mysqldb://root:sathya123#@localhost:3306/cricket")
    runs_overs=[]
    for i in range(1,21):
        delivery=pd.read_sql_query("select sum(total_runs) from deliveries where match_id=1 and inning=1 and `over`=%s ",params=[str(i)],con=my_conn)
        runs_overs.append(delivery.iloc[0]['sum(total_runs)'])
    overs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    data = {'overs': overs, 'runs': runs_overs}
    df = pd.DataFrame(data)

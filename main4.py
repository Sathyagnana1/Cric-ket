import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import mysql.connector
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
class main4:


    def teamstats():
        """

        :rtype: object
        """
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sathya123#",
            database="cricket"
        )



    teamstats()
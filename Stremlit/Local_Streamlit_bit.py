import streamlit as st 
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

dbconn = os.getenv('DBCONN')

def get_data ():
    conn = psycopg.connect(dbconn)
    # Create Cursor
    Cur = conn.cursor()
    
    Cur.execute('''
                select * from "Bitcoin_Data" ;
    ''')
    data = Cur.fetchall()
    conn.close()

    print(data)

    return data
data = get_data()

Bitcoin_Data_DF = 

st.title('Bitcoin Trend')


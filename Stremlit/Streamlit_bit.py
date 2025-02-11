## for local version just make visible commented out lines and just need to hide st.secreates line

import streamlit as st 
import pandas as pd
import numpy as np
import psycopg

# import os
# import dotenv
# from dotenv import load_dotenv
# load_dotenv()



def get_data ():
    #dbconn = os.getenv('DBCONN')
    dbconn = st.secrets['DBCONN'] # for local version need to comment out
    conn = psycopg.connect(dbconn)
    # Create Cursor
    Cur = conn.cursor()
    
    results = Cur.execute('''
                select * from "Bitcoin_Data" ;
                ''').fetchall()
    
    print (results)
    
    conn.commit()
    Cur.close()
    conn.close()
    
    Bitcoin_Date = []
    Bitcoin_Open = []
    Bitcoin_High = []
    Bitcoin_Low = []
    Bitcoin_Close = []
    Bitcoin_Volumn = []
    
    for row in results:
        Bitcoin_Date.append(row[0])
        Bitcoin_Open.append(row[0])
        Bitcoin_High.append(row[0])
        Bitcoin_Low.append(row[0])
        Bitcoin_Close.append(row[0])
        Bitcoin_Volumn.append(row[0])
    
    Bitcoin_Data_DF = pd.DataFrame({"Date": Bitcoin_Date, "Close": Bitcoin_Close})    
    return Bitcoin_Data_DF
    

results = get_data()

st.title('Bitcoin Trend')
st.dataframe(results)



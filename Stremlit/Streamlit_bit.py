import streamlit as st 
import pandas as pd
import psycopg


def get_data ():
    dbconn = st.secrets['DBCONN'] # for local version need to comment out
    conn = psycopg.connect(dbconn)
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
        Bitcoin_Open.append(row[1])
        Bitcoin_High.append(row[2])
        Bitcoin_Low.append(row[3])
        Bitcoin_Close.append(row[4])
        Bitcoin_Volumn.append(row[5])
    
    Bitcoin_Data_DF = pd.DataFrame({"Date": Bitcoin_Date, "Open": Bitcoin_Open, "High":Bitcoin_High, "Low" : Bitcoin_Low , "Close": Bitcoin_Close, "Volume" : Bitcoin_Volumn})    
    return Bitcoin_Data_DF
    

results = get_data()

st.title('Bitcoin Trend')
st.dataframe(results)
st.line_chart(data= results, x = "Date" , y= "Close")

st.title('Bitcoin News')



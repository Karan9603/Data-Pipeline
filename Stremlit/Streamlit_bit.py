import streamlit as st 
import pandas as pd
import psycopg
from datetime import datetime



st.title('Bitcoin Trend')

# Define months options
Six_M = 6
Three_M = 3
One_M = 1

options_M = [Six_M, Three_M, One_M]

# Use Streamlit's selectbox or radio button for selecting months
selection_M = st.selectbox("Select Time Period", options_M, index=0)  # Default to 6 months
#selection_M = st.pills("Select Time Period", options_M, selection_mode="single", index = 0)

# Get the current date
current_date = pd.to_datetime('today')

# Calculate the date X months ago
X_months_ago = current_date - pd.DateOffset(months=selection_M)

X_months_ago = X_months_ago.date()

# Display the final date as a string
st.write("Date for the selected period:", X_months_ago)


def get_bitcoin_data():
    dbconn = st.secrets['DBCONN'] # for local version need to comment out
    conn = psycopg.connect(dbconn)
    Cur = conn.cursor()
    
    # Use parameterized query to safely pass X_months_ago value to SQL
    query = '''select * from "Bitcoin_Data" where "Date" >= %s;'''
    results = Cur.execute(query, (X_months_ago,)).fetchall()
    

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

    Bitcoin_Data_DF = pd.DataFrame({
        "Date": Bitcoin_Date,
        "Open": Bitcoin_Open,
        "High": Bitcoin_High,
        "Low": Bitcoin_Low,
        "Close": Bitcoin_Close,
        "Volume": Bitcoin_Volumn
    })
    return Bitcoin_Data_DF

def get_bitcoin_news():
    dbconn = st.secrets['DBCONN'] # for local version need to comment out
    conn = psycopg.connect(dbconn)
    Cur = conn.cursor()

    results = Cur.execute('''select * from "Bitcoin_News";''').fetchall()

    conn.commit()
    Cur.close()
    conn.close()

    News_Heading = []
    News_Link = []
    News_Details = []
    Catagory_of_Article = []
    Date_of_Publication = []

    for row in results:
        News_Heading.append(row[0])
        News_Link.append(row[1])
        News_Details.append(row[2])
        Catagory_of_Article.append(row[3])
        Date_of_Publication.append(row[4])

    Bitcoin_News_DF = pd.DataFrame({
        "Heading": News_Heading,
        "Link": News_Link,
        "Details": News_Details,
        "Catagory_of_article": Catagory_of_Article,
        "Publication_Date" : Date_of_Publication
    })
    return Bitcoin_News_DF


# Fetch data
bitcoin_data_df = get_bitcoin_data()
bitcoin_news_df = get_bitcoin_news()

# Display Bitcoin Data

options = ["Open", "High", "Low", "Close", "Volume"]
#selection = st.radio("Daily_Value", options)  # Use st.radio or st.selectbox instead of st.pills
selection = st.pills("Daily_Value", options, selection_mode="single")
st.line_chart(data=bitcoin_data_df, x="Date", y=selection)

# Display Bitcoin News
st.title('Bitcoin News')
st.dataframe(bitcoin_news_df)


print (X_months_ago)



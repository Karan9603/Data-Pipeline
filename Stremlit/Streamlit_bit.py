import streamlit as st 
import pandas as pd
import psycopg



def get_bitcoin_data():
    dbconn = st.secrets['DBCONN'] # for local version need to comment out
    conn = psycopg.connect(dbconn)
    Cur = conn.cursor()

    results = Cur.execute('''select * from "Bitcoin_Data";''').fetchall()

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
st.title('Bitcoin Trend')
#st.dataframe(bitcoin_data_df)

options = ["Open", "High", "Low", "Close", "Volume"]
selection = st.pills("Daily_Value", options, selection_mode="single")

st.line_chart(data= bitcoin_data_df, x = "Date" , y= selection)

# Display Bitcoin News
st.title('Bitcoin News')
st.dataframe(bitcoin_news_df)



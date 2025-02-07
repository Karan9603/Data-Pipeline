import requests
import os 
from datetime import datetime

API_KEY = os.getenv("My_API_Key")


def get_data():
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey={API_KEY}"
    response = requests.get(url)
    values = response.json()
    #print(values)  # This will print the whole response from the API
    return values

def main () :
    # Get the data from the API
    data = get_data()

    # 'Time Series (Daily)' is the key where the date-based data is located in the API response
    time_series = data.get("Time Series (Digital Currency Daily)")

    # Get the current date
    #current_date = pd.to_datetime('today')
    #current_date = current_date.strftime("%Y-%m-%d")
    
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Filter the data to include only the last 6 months
    #six_months_ago = current_date - pd.DateOffset(months=6)

    Bitcoin_Date = []
    Bitcoin_Open = []
    Bitcoin_High = []
    Bitcoin_Low = []
    Bitcoin_Close = []
    Bitcoin_Volumn = []

    for date1, daily_values in time_series.items():
        #print(date1)
        #print(current_date)
        
        if (isinstance(daily_values, dict)) and ('1. open' in daily_values) and (date1== current_date):
            Bitcoin_Date.append(date1)
            Bitcoin_Open.append(float(daily_values["1. open"]))
            Bitcoin_High.append(float(daily_values['2. high']))
            Bitcoin_Low.append(float(daily_values['3. low']))
            Bitcoin_Close.append(float(daily_values['4. close']))
            Bitcoin_Volumn.append(float(daily_values['5. volume']))      
        # else:
        #     print(f"Unexpected structure for {date1}: {daily_values}")

    # Reverse the dates and opening values if needed to get the chronological order
    Bitcoin_Date.reverse()
    Bitcoin_Open.reverse()
    Bitcoin_High.reverse()
    Bitcoin_Low.reverse()
    Bitcoin_Close.reverse()
    Bitcoin_Volumn.reverse()
    
    return Bitcoin_Date + Bitcoin_Open + Bitcoin_High + Bitcoin_Low + Bitcoin_Close + Bitcoin_Volumn
    
import requests
import pandas as pd 
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates


my_key = 'DVC3S0LMT7YNYDC3'
  
# Method to retrieve data from the Alpha Vantage API given a stock symbol
def get_data(symbol: str):
   url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&datatype=csv&apikey={my_key}'
   
   data = requests.get(url)
   data = StringIO(data.text)
   data = pd.read_csv(data, index_col = 'timestamp', parse_dates=True)
   
   return data


# Method to plot data before running the model
def plot_data(data: pd.DataFrame, symbol: str, key: str, time: str, title: str):
   plt.figure(figsize=(15, 7))
   plt.plot(data.index, data[key])
   plt.xlim([data.index.min(), data.index.max()])
   plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
   
   # If we are using all time or just the last 30 days of data
   if time == 'year':
      plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))  # Change interval as needed
   elif time == 'day':
      plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
   
   # Since volume has a different y-axis label than the prices
   if key == 'volume':
      plt.ylabel('Amount')
   else:
      plt.ylabel('Price $USD')
   
   plt.xticks(rotation=40)
   plt.xlabel('Date')
   plt.title(f'{title} History For {symbol}')

   plt.show()
   

# Create sequences of x in order to predict y
def extract_seqX_outY(data: np.array, N: int, offset: int):
    '''
    # Data: My numpy array of data from the dataframe
    # N: My size that I want the sequence before to be
    # Offset: Where we want to start the split
    '''
    X, y = [], []

    for i in range(offset, len(data)):
         if i >= N:
            X.append(data[i - N:i])
            y.append(data[i][3])

    return np.array(X), np.array(y)
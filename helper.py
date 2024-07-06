import requests
import pandas as pd 
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates


my_key = 'DVC3S0LMT7YNYDC3'
  
  
def get_data(symbol: str):
   '''
   Method to retrieve data from the Alpha Vantage API given a stock symbol
   
   Parameters
   ----------
   # symbol: The stock we want to get data from
   '''
   url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&datatype=csv&apikey={my_key}'
   
   data = requests.get(url)
   data = StringIO(data.text)
   data = pd.read_csv(data, index_col = 'timestamp', parse_dates=True)
   
   return data


def plot_data(data: pd.DataFrame, symbol: str, key: str, time: str, title: str):
   '''
   Method to plot data before running the model based on given stock data
   
   Parameters
   ----------
   # data: My pandas dataframe of data to plot
   # symbol: The stock that we are analyzing
   # key: Which column of the dataframe we want to analyze
   # time: The time period we are analyzing (all time for year; past 30 trading days for day)
   # title: The title prefix for the graph
   '''
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
   

def extract_seqX_outY(data: np.array, N: int, offset: int):
   '''
   Part of the data preparation phase for the model
   Create sequences of x in order to predict y
   
   Parameters
   ----------
   # data: My numpy array of data from the dataframe
   # N: My size that I want the sequence before to be
   # offset: Where we want to start the split
   '''
   X, y = [], []

   for i in range(offset, len(data)):
      if i >= N:
         X.append(data[i - N:i])
         y.append(data[i][3])

   return np.array(X), np.array(y)
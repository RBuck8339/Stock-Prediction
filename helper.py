# Currently just imports the data and tests with it

import requests
import pandas as pd 
from io import StringIO


my_key = 'DVC3S0LMT7YNYDC3'
  
def get_data(symbol: str):
   url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&datatype=csv&apikey={my_key}'
   
   data = requests.get(url)
   data = StringIO(data.text)
   data = pd.read_csv(data, index_col = 'timestamp', parse_dates=True)
   
   return data

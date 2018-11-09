import json, urllib.request
import os
import plotly
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter, Layout

idx = 4
functype = ['TIME_SERIES_DAILY', 'TIME_SERIES_DAILY_ADJUSTED', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_WEEKLY_ADJUSTED',
            'TIME_SERIES_MONTHLY', 'TIME_SERIES_MONTHLY_ADJUSTED']

symbol = 'TSLA'
apikey = 'UAQTU7VRCE6C15QE'
url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&apikey={2}'.format(functype[idx], symbol, apikey)
timetype = ["Time Series (Daily)", "Weekly Time Series", "Weekly Adjusted Time Series", "Monthly Time Series",
            "Monthly Adjusted Time Series"]

series = 0 if idx <= 1 else idx-1

timeperiod = timetype[series]
data = urllib.request.urlopen(url).read()
stock_data = json.loads(data)

openval,  highval, lowval, closeval, volval, numval = ([] for num in range(6))
stock_keys = ['1. open','2. high','3. low','4. close','5. volume']

def fillstockarr(arr, value):
    for key in stock_data[timeperiod]:
        arr.append(float(stock_data[timeperiod][key][stock_keys[value]]))
        numval.append(key)

fillstockarr(openval,0)

plotly.offline.plot({
    "data": [Scatter(x=numval, y=openval)],
    "layout": Layout(title="Open Values")
}, filename="open_values")

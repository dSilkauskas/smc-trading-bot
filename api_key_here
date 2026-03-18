import requests
import pandas as pd

API_KEY = "3Z335B593GWN4SZK"
SYMBOL = "IBM"   # start with IBM, NOT NQ
INTERVAL = "5min"

url = (
    "https://www.alphavantage.co/query"
    f"?function=TIME_SERIES_INTRADAY"
    f"&symbol={SYMBOL}"
    f"&interval={INTERVAL}"
    f"&outputsize=full"
    f"&apikey={API_KEY}"
)

r = requests.get(url)
data = r.json()

key = f"Time Series ({INTERVAL})"
ts = data[key]

df = pd.DataFrame.from_dict(ts, orient="index")
df.index = pd.to_datetime(df.index)

df = df.rename(columns={
    "1. open": "open",
    "2. high": "high",
    "3. low": "low",
    "4. close": "close",
    "5. volume": "volume"
})

df = df.sort_index()

df.to_csv("ibm.csv")
print("Rows:", len(df))

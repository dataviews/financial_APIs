import requests
from constants import yahoo_headers
import pandas as pd

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-summary"

headers = yahoo_headers

querystring = {"region":"US"}

response = requests.request("GET", url, headers=headers, params=querystring)

df = pd.DataFrame(response)

print(df)
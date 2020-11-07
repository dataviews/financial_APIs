import yfinance as yf
import pandas as pd
import ssl
import datetime
import time
import seaborn as sns
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

ssl._create_default_https_context = ssl._create_unverified_context

# documentation here: https://github.com/ranaroussi/yfinance

tickers = ["MSFT", "BABA", "IBM"]


def include_keys(dictionary, keys):
    """Filters a dict by only including certain keys."""
    key_set = set(keys) & set(dictionary.keys())
    return {key: dictionary[key] for key in key_set}


def get_data(ticker):
    comp = yf.Ticker(ticker)
    print(comp)

    # get stock info
    info = comp.info

    print(np.mean(comp.dividends))
    hist_div = comp.dividends

    keep = ['regularMarketPreviousClose', 'industry', 'lastDividendValue', 'lastDividendDate',
            'fiveYearAvgDividendYield', 'dividendRate']

    temp_list = []

    filtered = include_keys(info, keep)
    filtered.update({'ticker': ticker})
    temp_list.append(filtered)

    # filtered = filtered.update({'ticker': ticker})
    df = pd.DataFrame(temp_list)
    # df['lastDividendDate'] = datetime.datetime.fromtimestamp(df['lastDividendDate']).isoformat()
    # df['lastDividendDate'] = pd.to_datetime(df['lastDividendDate'], format='%Y-%m-%dT%H:%M:%S')

    sns.distplot(hist_div, label=ticker)

    return df, info, hist_div


for ticker in tickers:
    get_data(ticker)
import yfinance as yf
import pandas as pd
import ssl
import datetime
import time
import seaborn as sns
import matplot.pyplot as plt
import numpy as np
import warnings
from stocks import *

warnings.simplefilter(action='ignore', category=FutureWarning)

ssl._create_default_https_context = ssl._create_unverified_context

# documentation here: https://github.com/ranaroussi/yfinance

def include_keys(dictionary, keys):
    """Filters a dict by only including certain keys."""
    key_set = set(keys) & set(dictionary.keys())
    return {key: dictionary[key] for key in key_set}


def get_data(ticker):
    comp = yf.Ticker(ticker)
    print(comp)

    # get stock info
    info = comp.info

    hist_div = comp.dividends
    mean_dividend = np.mean(comp.dividends)

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

    return df, info, hist_div, mean_dividend


for i, ticker in enumerate(tech):
    df, info, hist_div, mean_dividend = get_data(ticker)

    if len(hist_div) == 0:
        print("No dividends to graph")
        pass
    else:
        # plt.figure(i)
        # ax = sns.distplot(hist_div, bins = 50)
        # ax.set_title("Stock " + ticker)

        fig = plt.figure()
        ax = plt.axes()
        ax.plot(hist_div)
        ax.set_title("Stock " + ticker)

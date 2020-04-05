import pandas as pd
import numpy as np
import pickle


def preprocess_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv(
        "./python_programming_for_finance/sp500_joined_closes.csv", index_col=0)
    tickers = df.columns.values
    df.fillna(0, inplace=True)
    # print(df[ticker])
    # print(df.iloc[:3])
    # print(df[ticker].shift(-3))
    for d in np.arange(1, hm_days+1):
        df["{}_{}d".format(ticker, d)] = (
            df[ticker].shift(-d) - df[ticker]) / df[ticker]
    df.fillna(0, inplace=True)
    print(df)
    return tickers, df


preprocess_data_for_labels("XOM")

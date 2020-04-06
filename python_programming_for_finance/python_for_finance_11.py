from python_for_finance_9 import preprocess_data_for_labels
from python_for_finance_10 import buy_sell_hold
from collections import Counter
import numpy as np


def extract_featuresets(ticker):
    # Get target value
    tickers, df = preprocess_data_for_labels(ticker)
    df["{}_target".format(ticker)] = list(
        map(buy_sell_hold, *[df["{}_{}d".format(ticker, i)] for i in range(1, 8)]))
    # print(df)
    vals = df["{}_target".format(ticker)].values
    # print(vals)
    c = Counter(vals)
    print("Data spread: ", c)

    # Null value
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf, np.nan])
    df.dropna(inplace=True)

    # Percentange
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    # print(df_vals)
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    # X and y
    X = df_vals.values
    y = df["{}_target".format(ticker)].values
    # print(X, y)

    return X, y, df


extract_featuresets('XOM')

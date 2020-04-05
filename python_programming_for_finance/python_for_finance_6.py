import python_for_finance_5 as pyff5
import pickle
import os
import datetime as dt
import pandas as pd
import pandas_datareader.data as web


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = pyff5.save_sp500_tickers()
    else:
        with open("./python_programming_for_finance/sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    # print(tickers)

    if not os.path.exists('./python_programming_for_finance/stock_dfs'):
        os.makedirs('./python_programming_for_finance/stock_dfs')

    start = dt.datetime(2018, 4, 1)
    end = dt.datetime(2020, 4, 3)

    for ticker in tickers:
        if ticker.find(".") >= 0:
            ticker = ticker.replace(".", "-")
        # print(ticker)

        if not os.path.exists("./python_programming_for_finance/stock_dfs/{}.csv".format(ticker)):
            df = web.DataReader(ticker, "yahoo", start, end)
            df.to_csv(
                "./python_programming_for_finance/stock_dfs/{}.csv".format(ticker))
            print("Get {}".format(ticker))
        else:
            df = pd.read_csv(
                "./python_programming_for_finance/stock_dfs/{}.csv".format(ticker))
            print("Already have {}".format(ticker))
        print(df.head())


get_data_from_yahoo()


# start = dt.datetime(2018, 4, 1)
# end = dt.datetime(2020, 4, 3)
# df = web.DataReader('BRK-B', "yahoo", start, end)
# print(df)

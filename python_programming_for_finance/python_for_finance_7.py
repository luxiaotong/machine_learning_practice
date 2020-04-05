import pickle
import pandas as pd


def complie_data():
    with open("./python_programming_for_finance/sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        if ticker.find(".") >= 0:
            ticker = ticker.replace(".", "-")

        with open("./python_programming_for_finance/stock_dfs/{}.csv".format(ticker)) as f:
            df = pd.read_csv(f, index_col="Date")

        df = df[['Adj Close']]
        df.rename({"Adj Close": ticker}, axis="columns", inplace=True)

        # print(ticker)
        # print(df.head())

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how="outer")

        if count % 10 == 0:
            print(count)

    print(main_df)
    main_df.to_csv("./python_programming_for_finance/sp500_joined_closes.csv")


complie_data()

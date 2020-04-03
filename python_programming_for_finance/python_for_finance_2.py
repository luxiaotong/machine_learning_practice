import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start = dt.datetime(2018, 4, 1)
# end = dt.datetime(2020, 4, 3)

# df = web.DataReader('TSLA', 'yahoo', start, end)
# df.to_csv('./python_programming_for_finance/tsla.csv')
# print(df.head())

df = pd.read_csv('./python_programming_for_finance/tsla.csv',
                 parse_dates=True, index_col=0)
print(df['Adj Close'].head())
print(df[['Open', 'High']].head())
# df.plot()
# df['Adj Close'].plot()
# plt.show()

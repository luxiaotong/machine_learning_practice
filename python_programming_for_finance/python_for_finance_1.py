import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020, 4, 1)
end = dt.datetime(2020, 4, 3)

df = web.DataReader('TSLA', 'yahoo', start, end)
print(df)

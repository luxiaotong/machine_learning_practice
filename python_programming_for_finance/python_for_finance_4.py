import datetime as dt
import pandas as pd
import pandas_datareader.data as web

import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import dates
import mplfinance as mpf


style.use('ggplot')

df = pd.read_csv('./python_programming_for_finance/tsla.csv',
                 parse_dates=True, index_col=0)

df = df.iloc[-100:]
print(df)

# https://nbviewer.jupyter.org/github/matplotlib/mplfinance/blob/master/examples/customization_and_styles.ipynb
mc = mpf.make_marketcolors(up='r', down='g')
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, mav=(2, 20), type='candle', volume=True, style=s)

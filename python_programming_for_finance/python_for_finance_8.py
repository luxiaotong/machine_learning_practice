import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm


def visualize_data():
    df = pd.read_csv(
        "./python_programming_for_finance/sp500_joined_closes.csv")
    # df["AAPL"].plot()
    df_corr = df.corr()
    # print(df_corr.sample(10))
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    heatmap = ax.pcolormesh(data, cmap=plt.get_cmap("RdYlGn"))
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_lables = df_corr.columns
    # rows_lables = df_corr.index
    # print(column_lables)
    # print(rows_lables)
    ax.set_xticklabels(column_lables, rotation=90)
    ax.set_yticklabels(column_lables)
    # ax.set_yticklabels(rows_lables)
    heatmap.set_clim(-1, 1)

    plt.tight_layout()
    plt.show()


visualize_data()

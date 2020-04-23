import pandas as pd
from scipy.stats import iqr
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel("./data/statistics_mendenhall/EPAGAS.xls")
print(df.describe())

IQR = iqr(df)
s = df.std()
print("IQR: %.3f, standard deviation: %.3f, IQR/s: %.3f\n" % (IQR, s, IQR/s))

# df.hist()
# plt.hist(df.to_numpy())
stats.probplot(df["MPG"], plot=plt)

plt.show()

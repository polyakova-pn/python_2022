import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

#пункт 1
a = ((diamonds["x"] > 5) | (diamonds["y"] > 5) | (diamonds["z"] > 5))
print('пункт 1')
print(diamonds[a])

#пункт 2
notinfl = diamonds.select_dtypes(include = ['object'])
print('пункт 2')
print(notinfl)

#пункт 3
infl = diamonds.select_dtypes(include = ['float64', 'int64'])
print('пункт 3')
print(infl.mean())

#пункт 4
meanprice = diamonds.groupby(["cut"]).agg({"price":"mean"})
meanprice.plot(kind = "bar")
plt.show()

#пункт 5
plt.hist(diamonds['carat'], bins = 100)
plt.show()

#пункт 6
print('пункт 6')
print((pd.isna(diamonds).sum()).sum())

#пункт 7
print('пункт 7')
print(diamonds)

#пункт 8
print('пункт 8')
print(diamonds.memory_usage().sum())

#пункт 8
print('пункт 8')
def rs20(x):
    index = np.sort(random.sample(range(len(diamonds)), 20))
    return diamonds.iloc[index]
print(rs20(diamonds))



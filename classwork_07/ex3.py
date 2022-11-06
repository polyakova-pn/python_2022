import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

#пункт 1
print('пункт 1')
titanic.groupby(["pclass"]).agg("count")
titanic.groupby(["age"]).agg("count")

#пункт 2
print('пункт 2')
def g(clas, SEX):
    sort = titanic[(titanic['pclass'] == clas) & (titanic['sex'] == SEX)].sort_values(by = "age", ascending = False)
    g1 = sort[:len(sort) // 2]
    g2 = sort[len(sort) // 2:]
    return g1, g2


for clas in [1, 2, 3]:
    for SEX in ['female', 'male']:
        print(g(clas, SEX))

#пункт 3
print('пункт 3')
omen_c1, ymen_c1 = g(1, 'male')
omen_c2, ymen_c2 = g(2, 'male')
omen_c3, ymen_c3 = g(3, 'male')
ofem_c1, yfem_c1 = g(1, 'female')
ofem_c2, yfem_c2 = g(2, 'female')
ofem_c3, yfem_c3 = g(3, 'female')

vyzh = pd.DataFrame({"male younger": [ymen_c1['survived'].mean(), ymen_c2['survived'].mean() , ymen_c3['survived'].mean()],
"male older": [omen_c1['survived'].mean(), omen_c2['survived'].mean() , omen_c3['survived'].mean()],
"female younger": [yfem_c1['survived'].mean(), yfem_c2['survived'].mean() , yfem_c3['survived'].mean()],
"female older": [ofem_c1['survived'].mean(), ofem_c2['survived'].mean() , ofem_c3['survived'].mean()]}, index = ["1", "2", "3"])
print(vyzh)

#пункт 4
print('пункт 4')
fm = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 1)].agg({'age': 'mean'})[0]
m = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 1)].agg({'age': 'mean'})[0]
print("females: ", fm, "males: ", m)

#пункт 5
print('пункт 5')
titanic[titanic['survived'] == 1]['age'].std()

#пункт 6
print('пункт 6')
arx = [i for i in range(0, 100, 5)]
ary = []
for i in range(20):
    ary.append(titanic[(titanic['age'] >= 5*i) & (titanic['age'] < 5 * (i + 1))].agg({'survived': 'mean'})[0])
plt.title("доля выживших от возраста")
plt.bar(arx, ary)
plt.show()


#пункт 7
print('пункт 7')
xf = []
yf = []
for i in range(20):
    yf.append(titanic[(titanic['age'] >= 5 * i) & (titanic['age'] < 5 * (i + 1)) & (titanic['sex'] == 'female')].agg({'survived': 'mean'})[0])
    xf.append(i * 5)
xm = []
ym = []
for i in range(20):
    ym.append(titanic[(titanic['age'] >= 5 * i) & (titanic['age'] < 5 * (i+1)) & (titanic['sex'] == 'male')].agg({'survived': 'mean'})[0])
    xm.append(i * 5)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(xf, yf, label = 'женщины')
plt.legend()
ax2.bar(xm, ym, label = 'мужчины')
plt.legend()
plt.show()

#пункт 8
print('пункт 8')
print(titanic["fare"].sum())
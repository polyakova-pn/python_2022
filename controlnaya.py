import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import random


def task_11():
    f = pd.read_csv("infile.csv")
    print(f.isnull().sum())

def task_12():
    f = pd.read_csv("video-games.csv")

    n_games = len(f['title'].value_counts())

    by_years = f.groupby(["year"]).agg({"title": "count"})

    mean_price = f.groupby(["publisher"]).agg({"price": "mean"})

    age_max_price = f.groupby(["age_raiting"]).agg({"price": "max"})

    d = {'n_games' : n_games, 'by_years' : by_years, 'mean_price': mean_price,'age_max_price': age_max_price}
    return d

def task_1():
    print(int(input()) ** 2 + int(input()) ** 2)
def task_2():
    s = str(input())
    ss = 'qwertyuiopasdfghjklzxcvbnm'
    ans = []
    for i in s:
        if s in ss:
            ans.append(i)
    print(*ans)
def task_3():
    slov = input().split()
    ans = 0
    for i in slov:
        if len(i) > 2 and i[-3:] == 'bus':
            ans += 1
    print(ans)

def pr(f, x):
    return (f(x + 0.0000001) - f(x)) / 0.0000001

def task_8(f, min_x, max_x, N, min_y, max_y):
    fig = plt.figure(figsize=(6.4, 4.8))
    ax = fig.add_subplot()
    arx = np.arange(min_x, max_x, (max_x - min_x) / N)
    ary = f(arx)
    ax.plot(arx, ary,'--', color = 'b')
    aryp = pr(f, arx)
    ax.plot(arx, aryp)
    ax.set_xlim([min_x, max_x])
    ax.set_ylim([min_y, max_y])
    ax.set_xscale('log')
    plt.grid()
    plt.savefig('function.pdf')
    plt.show()
def task_7():
    np.random.seed(8)
    mat = np.random.randint(1, 50, (7, 7))
    mino = mat[0:6, 0:6]
    return mat, np.linalg.det(mino)
def task_6(a1, a2, a3, a4):
    s1 = set(a1)
    s2 = set(a2)
    s3 = set(a3)
    s4 = set(a4)
    s = s1 | s2
    ss = s3 | s4
    ans = s & ss
    return ans


def task_5(ar):
    return ar[5:-1:2]

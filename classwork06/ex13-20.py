import pandas as pd
import numpy as np
import random

f = pd.read_csv("telecom_churn.csv")

print()
print('ex13')
intlmean = f[['Total intl calls']].mean()['Total intl calls']
print(intlmean)

print()
print('ex15')
inchf = f['Total day charge'][f.Churn == False].sum()
incht = f['Total day charge'][f.Churn == True].sum()
if incht > inchf:
    print('оставшихся меньше')
else:
    print('ушедших меньше')

print()
print('ex16')
ans16 = f.groupby(["State"]).agg({"Total day charge": "mean"}).sort_values(by="Total day charge", ascending = True)
print(*ans16.index)

print()
print('ex17')
print(f.groupby('Area code').mean())

print()
print('ex18')
ans18 = f.loc[[100, 102, 104], ["State", "Churn"]]
print(ans18)

print()
print('ex19')
ndf = pd.DataFrame({"x": np.random.rand(10), "y": np.random.rand(10)})
ndf["x^2 + y^2"] = (ndf["x"])**2 + (ndf["y"])**2
print(ndf)

print()
print('ex20')
ndf['mean'] = ndf[["x", "y", "x^2 + y^2"]].apply(lambda x: x.mean(), axis=1)
print(ndf)
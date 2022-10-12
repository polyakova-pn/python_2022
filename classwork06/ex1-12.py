import pandas as pd
import numpy as np
import random


print('ex3')
f = pd.read_csv("telecom_churn.csv")
tmean = f[['Total day calls']].mean()['Total day calls']
print(tmean)

print()
print('ex4')
print(f.groupby(["State"]).agg({"Total day calls": "mean"}).loc["LA"])

print()
print('ex5')
tdc = f.groupby(["State"]).agg({"Total day calls": "mean"})
print(tdc)

print()
print('ex6')
tdc_overmean = tdc[tdc['Total day calls'] >= tmean]
print(tdc_overmean)

print()
print('ex7')
day_eve = f.groupby(["State"]).agg({"Total day calls": "mean", "Total eve calls": "mean"})
print(day_eve)

print()
print('ex8')
day_eve['d > e'] = day_eve["Total day calls"] > day_eve["Total eve calls"]
print(day_eve)

print()
print('ex9')
f['obaplana'] = (f['International plan'] == 'Yes') & (f["Voice mail plan"] == 'Yes')
doly = f[['obaplana']].mean()
print(doly)

print()
print('ex10')
uac = f['Area code'].nunique()
print(uac)

print()
print('ex11')
servcalls = f.groupby(["Customer service calls"]).agg({"Customer service calls": "count"})
print(servcalls)

print()
print('ex12')
sc = f.groupby(["Customer service calls"]).agg({"Churn": "mean"})
print(sc)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.scatter(sc.index.values, sc['Churn'])
ax.set_xlabel('Customer service calls')
ax.set_ylabel('Churn doly')
plt.grid()
plt.show()
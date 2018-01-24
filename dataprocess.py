# -*- coding: utf-8 -*-
import pandas as pd


data = pd.read_csv("data.csv")
idokeido = pd.read_csv("ido_keido.csv")

print(data.head())
print(data.ix[2,:])
print(data.ix[2,:].isnull())
print(data.columns[1])

print(data.isnan())
#print(pd.concat(data_pr, data))
data_pr = pd.DataFrame(data.ix[:,0])
print(data.head())
for num, tf in enumerate(data.ix[2,:].isnull()):
    if tf:
        data_pr = pd.concat([data_pr, data.ix[:,num]], axis=1)

print(data_pr)

data_pr.to_csv("data_pr.csv", encoding="SHIFT-JIS")


data_after = pd.read_csv("data_pr.csv", encoding="SHIFT-JIS")
print(data_after.head(2))
data_dr = data_after.dropna(axis=1)
print(data_dr)
data_dr.to_csv("data_dr.csv", encoding="SHIFT-JIS")


print(idokeido.head(2))

d = pd.read_csv("kisyoudata.csv")
d_aa = pd.read_csv("kisyoudata_aa.csv")
print(d_aa.head(2))

name_idokeido = [i for i in idokeido.ix[:,1]]
print(idokeido[idokeido["地点"]=="野母崎"])
print(idokeido[idokeido["地点"]=="野母崎"]["緯度"])

print(idokeido["地点"])
for num, name in enumerate(d.ix[:,0]):
    if name in name_idokeido:
        d["緯度"][num] = idokeido[idokeido[name]=="野母崎"]["緯度"]

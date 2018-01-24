# -*- coding: utf-8 -*-
import pandas as pd
import os

print(os.getcwd())

data = pd.read_csv("kisyou_ido_keido_dropna.csv", encoding="SHIFT-JIS")
print(data.head())

data_pr = data.ix[:,2:-2]
print(data_pr.head())

from sklearn.cluster import KMeans

km = KMeans(n_clusters=20)
km.fit(data_pr)
labels = km.predict(data_pr)

print(labels)

data["cluster"] = labels
print(data.head())
data.to_csv("kisyou_cluster_20.csv", encoding="SHIFT=JIS")


data = pd.read_csv("kisyou_cluster_20_cr.csv",encoding="SHIFT-JIS")
data.ix[:,-1]
for i in range(len(data)):
    if data.ix[i,-1] == 10: data.ix[i,-1] = 1
    elif data.ix[i,-1] == 2: data.ix[i,-1] = 2
    elif data.ix[i,-1] == 18: data.ix[i,-1] = 3
    elif data.ix[i,-1] == 13: data.ix[i,-1] = 4
    elif data.ix[i,-1] == 5: data.ix[i,-1] = 5
    elif data.ix[i,-1] == 6: data.ix[i,-1] = 6
    elif data.ix[i,-1] == 12: data.ix[i,-1] = 7
    elif data.ix[i,-1] == 9: data.ix[i,-1] = 8
    elif data.ix[i,-1] == 1: data.ix[i,-1] = 9
    elif data.ix[i,-1] == 15: data.ix[i,-1] = 10
    elif data.ix[i,-1] == 17: data.ix[i,-1] = 11
    elif data.ix[i,-1] == 3: data.ix[i,-1] = 12
    elif data.ix[i,-1] == 16: data.ix[i,-1] = 13
    elif data.ix[i,-1] == 7: data.ix[i,-1] = 14
    elif data.ix[i,-1] == 8: data.ix[i,-1] = 15
    elif data.ix[i,-1] == 0: data.ix[i,-1] = 16
    elif data.ix[i,-1] == 14: data.ix[i,-1] = 17
    elif data.ix[i,-1] == 11: data.ix[i,-1] = 18
    elif data.ix[i,-1] == 19: data.ix[i,-1] = 19
    elif data.ix[i,-1] == 4: data.ix[i,-1] = 20

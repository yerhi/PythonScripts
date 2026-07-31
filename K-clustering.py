# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:29:53 2021

@author: u0136350
"""


# K-clustering

import pandas as pd

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt



data = pd.read_csv('C:/Users/u0136350/Documents/KU_Brain/GABA/Metabolites_correctedByTissueComposition_woOutliersOron.csv', na_values='', sep=',')
#data_m = pd.read_csv('G:/KU_Leuven/GABA/MetabolitesT.csv', na_values='', sep=';', decimal=",")


data = pd.read_csv()

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kemans.fit(segmentation_std)
    wcss.append(kmeans.inertia_)
    
plt.figure(figsize=(10,8))

plt.plot(range(1,11), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('K-means Clustering')
plt.show() 

#decidir el número de cluster de acuerdo a la regla del codo

kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
kmeans.fit(segmentation_std)  
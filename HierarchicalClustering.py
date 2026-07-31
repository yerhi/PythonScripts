# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:06:11 2021

@author: u0136350
"""


# Python 3.7 GRN Metabolites project
# Metabolites file: missing values were imputed (with average of age group). (except porone row which was fully deleted because only data from LSAM1 was available)

#Note: it seems that to transform to data frame, pandas only likes CSV - MSDOS // Or the separator used when reading the csv file
#To change commas to dots in excel go to File , Advanced, uncheck the Use system separators case and place dot in both next cases

# https://www.mltut.com/hierarchical-clustering-in-python-step-by-step-complete-guide/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.cluster.hierarchy as shc


from pylab import rcParams

from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm 
from sklearn.preprocessing import scale

from sklearn.preprocessing import StandardScaler, normalize

# Cluster subjects

data = pd.read_csv('C:/Users/u0136350/Documents/KU_Brain/GABA/Metabolites_correctedByTissueComposition_woOutliersMocaAndReplacingZ325_forHC.csv', na_values='', sep=',')
#data = pd.read_csv('G:/KU_Leuven/GABA/Metabolites.csv', na_values='', sep=';')

cols = ['LSM1_NAA','LSM1_Cho','LSM1_Cr','LSM1_Glx','LSM1_mIns','RSM1_NAA','RSM1_Cho','RSM1_Cr','RSM1_Glx','RSM1_mIns','LSTR_NAA','LSTR_Cho','LSTR_Cr','LSTR_Glx','LSTR_mIns','RSTR_NAA','RSTR_Cho','RSTR_Cr','RSTR_Glx','RSTR_mIns','OCC_NAA','OCC_Cho','OCC_Cr','OCC_Glx','OCC_mIns','PreSMA_NAA','PreSMA_Cho','PreSMA_Cr','PreSMA_Glx','PreSMA_mIns','RIFG_NAA','RIFG_Cho','RIFG_Cr','RIFG_Glx','RIFG_mIns']

df = pd.DataFrame(data, columns = cols)

sc = StandardScaler()
dfscaled = sc.fit_transform(df)
df_normalized = normalize(dfscaled)


df_normalized = pd.DataFrame(df_normalized, columns=cols)

plt.figure(figsize=(20,14))

plt.title('Clustering according to metabolites values')

dend = shc.dendrogram(shc.linkage(dfscaled, method='ward'))

plt.axhline(y=.5,color='r', linestyle='--')

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean',linkage='ward')

cluster.fit_predict(dfscaled)


sns.clustermap(dfscaled, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), xticklabels=True)


plt.figure(figsize=(20,14))
plt.scatter(df_scaled['RSM1_Glx'], df_scaled['RSM1_mIns'], c=cluster.labels_)

#Testing diffferent models https://www.datasciencelearner.com/how-to-do-hierarchical-clustering-in-python/

###########################################################################################################
#Cluster metabolites 

data_m = pd.read_csv('C:/Users/u0136350/Documents/KU_Brain/GABA/Metabolites_correctedByTissueComposition_woOutliersMocaAndReplacingZ325_forHC.csv', na_values='', sep=',', decimal=",")
#data_m = pd.read_csv('G:/KU_Leuven/GABA/MetabolitesT.csv', na_values='', sep=';', decimal=",")
#data_m = pd.read_csv('G:/KU_Leuven/GABA/MetabolitesT.csv', na_values='', sep=';', decimal=",")
#cols_s = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58']
#df_m = pd.DataFrame(data_m, columns = cols_s)




cols = ['LSM1_NAA','LSM1_Cho','LSM1_Cr','LSM1_Glx','LSM1_mIns','RSM1_NAA','RSM1_Cho','RSM1_Cr','RSM1_Glx','RSM1_mIns','LSTR_NAA','LSTR_Cho','LSTR_Cr','LSTR_Glx','LSTR_mIns','RSTR_NAA','RSTR_Cho','RSTR_Cr','RSTR_Glx','RSTR_mIns','OCC_NAA','OCC_Cho','OCC_Cr','OCC_Glx','OCC_mIns','PreSMA_NAA','PreSMA_Cho','PreSMA_Cr','PreSMA_Glx','PreSMA_mIns','RIFG_NAA','RIFG_Cho','RIFG_Cr','RIFG_Glx','RIFG_mIns']


df = pd.DataFrame(data_m, columns = cols)

dft = df.transpose()

sc = StandardScaler()

dftscaled = sc.fit_transform(dft)

dft_normalized = normalize(dftscaled)

#df_t = pd.DataFrame(dft_normalized, columns = cols)


plt.figure(figsize=(20,14))
dend_m = shc.dendrogram(shc.linkage(dft_normalized, method='ward'), leaf_rotation=45, leaf_font_size=11, show_contracted=True)





k = 3

HClustering = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage="ward")

All = HClustering.fit_predict(df_t)

sns.clustermap(dft_normalized, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), yticklabels=True)
clustergrid.dendrogram_row.reordered_ind

---------------------------------------

plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


HClustering.fit(data_scaled)

sm.accuracy_score(target, HClustering.labels_)


################################################################### BY PRINCIPAL COMPONENTS
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as hc
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering 
# Drop the customer id column
#
#df = df.drop('CUST_ID', axis = 1)
#
# Fill the missing values with ffill method
#
#df.fillna(method ='ffill', inplace = True) 
df_t = df.transpose()
# Scale the data and normalize
#
sc = StandardScaler()
dft_scaled = sc.fit_transform(df_t)
dft_normalized = normalize(dft_scaled)
#
# Reduce the dimensionality of data to 3 features
#
pca = PCA(n_components=3)
df_pca = pca.fit_transform(dft_normalized)
df_pca = pd.DataFrame(df_pca)
df_pca.columns = ['P1', 'P2', 'P3']
#
# Create the Dendogram plot
#

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean',linkage='ward')

cluster.fit_predict(dft_normalized)





plt.figure(figsize =(24, 24))
plt.title('Visualising the data')
dendrogram = hc.dendrogram((hc.linkage(df_pca, method ='ward'), leaf_font_size=45))

# leaf_font_size=11,

sns.clustermap(df_pca, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), yticklabels=True)

sns.clustermap(df, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), yticklabels=True)

sns.clustermap(dft_normalized, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), yticklabels=True)




agc = AgglomerativeClustering(n_clusters = 2)
plt.figure(figsize =(8, 8))
plt.scatter(df_pca['P1'], df_pca['P2'], c = agc.fit_predict(df_pca), cmap ='rainbow')
plt.title("Agglomerative Hierarchical Clusters - Scatter Plot", fontsize=18)
plt.show() 

# standarise non-normalised data and use correlation to make the heatmap
sns.clustermap(df_t,
               metric="correlation",
               standard_scale=1)
plt.savefig('G:/KU_Leuven/GABA/Figures/HeatmapMetabolitesCorrelationStadarisedData.png',dpi=150)


##### Apparently hierarchical clustering for correlation matrix is not usually a thing but to explore:


CorrM = df.corr(method='pearson')


# CorrM.to_excel('G:/KU_Leuven/GABA/CorrelationMatrix.xlsx')


sns.heatmap(CorrM, annot=True)
plt.show()

sns.clustermap(CorrM, metric = 'euclidean', cmap = 'coolwarm', figsize = (7,7), yticklabels=True)
 


df['PreSMA_NAA'].corr(df['LSTR_NAA'])


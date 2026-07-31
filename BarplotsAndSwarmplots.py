# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:51:18 2022

@author: u0136350
"""


### Bar plots merged with swarm plots (or strip plots) /w data points/

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load some example data
#tips = sns.load_dataset("tips")




# https://stackoverflow.com/questions/68154123/matplotlib-grouped-bar-chart-with-individual-data-points



#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/ FOR NEUROCHEMICAL NETWORKS PAPER
#data = pd.read_csv('C:/Users/u0136350/Documents/KU_Brain/GABA/Python/SwarmplotsNeurochemicalNetworks.csv', na_values='', sep=',')


cols = ['group','GROUP','Region','mIns']

df = pd.DataFrame(data, columns = cols)



NAA = ['LSM1_NAA','RSM1_NAA','LSTR_NAA','RSTR_NAA','PreSMA_NAA','RIFG_NAA','OCC_NAA']
Cho = ['LSM1_Cho','RSM1_Cho','LSTR_Cho','RSTR_Cho','PreSMA_Cho','RIFG_Cho','OCC_Cho']
Cr = ['LSM1_Cr','RSM1_Cr','LSTR_Cr','RSTR_Cr','PreSMA_Cr','RIFG_Cr','OCC_Cr']
Glx = ['LSM1_Glx','RSM1_Glx','LSTR_Glx','RSTR_Glx','PreSMA_Glx','RIFG_Glx','OCC_Glx']
mIns = ['LSM1_mIns','RSM1_mIns','LSTR_mIns','RSTR_mIns','PreSMA_mIns','RIFG_mIns','OCC_mIns']



df_NAA = pd.DataFrame(data, columns = NAA)
df_Cho = pd.DataFrame(data, columns = Cho)
df_Cr = pd.DataFrame(data, columns = Cr)
df_Glx = pd.DataFrame(data, columns = Glx)
df_mIns = pd.DataFrame(data, columns = mIns)


GROUP = df['GROUP']

gp = df['group']


#data_young = data[data['AGE']<40]
#data_old = data[data['AGE']>40] 
#df_young_NAA = pd.DataFrame(data_young, columns = NAA)
#df_old_NAA = pd.DataFrame(data_old, columns = NAA)


#df_young[df_young<.000001]=np.nan #to exclude values equal to zero -missing data- in correlation. exchange zeros for NaN
#df_old[df_old<.000001]=np.nan 


# Draw the bar chart
ax = sns.violinplot(
    data=df, 
    x=df['Region'], 
    y=df['mIns'],
    hue=df['GROUP'],
   # estimator=np.mean['NAA'],
    alpha=0.7, 
    ci=None,
    palette=['lightcyan','lightyellow'], # palette=['skyblue','lemonchiffon'],
    labels=None
)

# Get the legend from just the bar chart
#handles, labels = ax.get_legend_handles_labels()

# Draw the stripplot, swarmplot   //// the violin plot and the swamplot alone (without barplot look better 

#plt.figure(figsize=(7,7))
sns.swarmplot(
    data=df, 
    x=df['Region'], 
    y=df['mIns'], 
    hue=df['GROUP'], 
    dodge=True, 
    edgecolor="black", 
    linewidth=.75,
    palette=['cyan','yellow']

 #   ax=ax,
)
# Remove the old legend
ax.legend_.remove()
# Add just the bar chart legend back
ax.legend(
    handles,
    labels,
    loc=7,
    bbox_to_anchor=(1.25, .5),
)



....



#data = pd.read_csv('C:/Users/u0136350/Documents/KU_Brain/GABA/Metabolites_correctedByTissueComposition_woOutliersOron.csv', na_values='', sep=',')
#data_m = pd.read_csv('G:/KU_Leuven/GABA/MetabolitesT.csv', na_values='', sep=';', decimal=",")


#cols = ['LSM1_NAA','RSM1_NAA','LSTR_NAA','RSTR_NAA','PreSMA_NAA','RIFG_NAA','OCC_NAA','LSM1_Cho','RSM1_Cho','LSTR_Cho','RSTR_Cho','PreSMA_Cho','RIFG_Cho','OCC_Cho','LSM1_Cr','RSM1_Cr','LSTR_Cr','RSTR_Cr','PreSMA_Cr','RIFG_Cr','OCC_Cr','LSM1_Glx','RSM1_Glx','LSTR_Glx','RSTR_Glx','PreSMA_Glx','RIFG_Glx','OCC_Glx','LSM1_mIns','RSM1_mIns','LSTR_mIns','RSTR_mIns','PreSMA_mIns','RIFG_mIns','OCC_mIns'] 


#df = pd.DataFrame(data, columns = cols)

#data_young = data[data['AGE']<40]
#data_old = data[data['AGE']>40] 
#df_young = pd.DataFrame(data_young, columns = cols)
3df_old = pd.DataFrame(data_old, columns = cols)

##df=df.fillna(0)    #to replace NaN for zeros, but Metabolites database imputed NaN with Average (very few)
##df['LSM1_NAA'].dtype
##LSM1_NAA_int=data['LSM1_NAA'].astype(np.int)


#*/*/*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*CORRELATION*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

df_young[df_young<.000001]=np.nan #to exclude values equal to zero -missing data- in correlation. exchange zeros for NaN
df_old[df_old<.000001]=np.nan 

CorrYoung = df_young.corr()
CorrOld = df_old.corr()
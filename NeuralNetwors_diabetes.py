# -*- coding: utf-8 -*-
"""
Created on Wed May 28 15:37:17 2025

@author: u0136350
"""


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import all_pairs_node_connectivity
from networkx.algorithms.approximation import local_node_connectivity
from networkx.algorithms.approximation import node_connectivity
from networkx.algorithms.assortativity import average_degree_connectivity
from networkx.algorithms import approximation
from networkx.algorithms.smallworld import random_reference 


#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTRAREGIONAL NETWORKS FULL SAMPLE 


MultiG = nx.MultiGraph()


LHIPP = nx.Graph()
mPFC = nx.Graph()
LSM1 = nx.Graph()
PCC = nx.Graph()




grafitos = [mPFC, LSM1, PCC, LHIPP]

for i in grafitos:

    i.add_node('GABA+', color = 'red')
    i.add_node('Glx', color = 'green')
    i.add_node('Glu', color = 'darkgreen')
    i.add_node('Gln', color = 'lightgreen')
    i.add_node('GSH', color = 'blue')
    i.add_node('mI', color = 'magenta')
    i.add_node('tNAA', color = 'yellow')
    i.add_node('tCho', color = 'green')
    i.add_node('tCr', color = 'purple')
    i.add_node('Lac', color = 'pink')




edges_LHIPP = [('Glx','tCr',0.439),
              ('GSH','tCr',0.567),('mI','tCho',.59),
              ('mI','tCr',0.58),('tNAA','tCho',.491),('tNAA','tCr',.604), 
              ('tCho','tCr',.597)] #mcc

edges_mPFC = [('Glx','Glu',.922),('Glx','Gln',.698),
              ('tNAA','tCho',.474),('tNAA','tCr',.649)] #mcc

edges_LSM1 = [('Glx','Glu', .921),('Glx','Gln',.769),('Glx','mI',.459),
              ('Glu','Gln',.515),
              ('mI','tCr',.463),('tNAA','tCr',.442)] #mcc ,('Glu','mI',.39),,('Glu','NAA',.341)

edges_PCC = [('Glx','Glu',.945),('Glx','Gln',.709),('Glx','mI',.487),('Glu','Gln',.498),
             ('Glu','mI',.469),('Gln','GSH',.477),('Gln','tNAA',.440),
             ('mI','tCho',.460),('tNAA','tCho',.517),('tNAA','tCr',.733)] #mcc



for i in grafitos:
    print(i)
    print('Degree connectivity', nx.degree(i))


#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%




LHIPP.add_weighted_edges_from(edges_LHIPP) #adds the edges
widths = nx.get_edge_attributes(LHIPP, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LHIPP)
nx.draw_networkx_nodes(LHIPP,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(LHIPP,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LHIPP, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
#ax.set(ylim=(2,5))
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])


plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

mPFC.add_weighted_edges_from(edges_mPFC) #adds the edges
widths = nx.get_edge_attributes(mPFC, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mPFC)
nx.draw_networkx_nodes(mPFC,pos,
                       node_size=700,
                       node_color='tomato',
                       alpha=0.7)
nx.draw_networkx_edges(mPFC,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mPFC, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

LSM1.add_weighted_edges_from(edges_LSM1) #adds the edges
widths = nx.get_edge_attributes(LSM1, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LSM1)
nx.draw_networkx_nodes(LSM1,pos,
                       node_size=700,
                       node_color='plum',
                       alpha=0.7)
nx.draw_networkx_edges(LSM1,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LSM1, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

PCC.add_weighted_edges_from(edges_PCC) #adds the edges
widths = nx.get_edge_attributes(PCC, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(PCC)
nx.draw_networkx_nodes(PCC,pos,
                       node_size=700,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(PCC,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(PCC, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTRAREGIONAL NETWORKS CONTROLS 
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*


LHIPPc = nx.Graph()
mPFCc = nx.Graph()
LSM1c = nx.Graph()
PCCc = nx.Graph()


# edges = Significant correlation controlling for local GM (for now wo mcc)

grafitos_c = [LHIPPc, mPFCc, LSM1c, PCCc]





for i in grafitos_c:

    i.add_node('GABA+', color = 'red')
    i.add_node('Glx', color = 'green')
    i.add_node('Glu', color = 'darkgreen')
    i.add_node('Gln', color = 'lightgreen')
    i.add_node('GSH', color = 'blue')
    i.add_node('mI', color = 'magenta')
    i.add_node('tNAA', color = 'yellow')
    i.add_node('tCho', color = 'green')
    i.add_node('tCr', color = 'purple')
    i.add_node('Lac', color = 'pink')





edges_LHIPPc = [('GSH','mI',0.481),('GSH','tCr',0.593),('mI','tCho',0.635),
               ('mI','tCr',.748),
               ('tCho','tCr',.625)] #mcc

edges_mPFCc = [('Glx','Glu',.942),('Glx','Gln',.761),('GSH','tCr',.757)] #mcc

edges_LSM1c = [('Glx','Glu',.957)] #mcc
             

edges_PCCc = [('Glx','Glu',.947),('Glx','Gln',.708),('tNAA','tCr',.668)] #mcc


LHIPPc.add_weighted_edges_from(edges_LHIPPc)
mPFCc.add_weighted_edges_from(edges_mPFCc)
LSM1c.add_weighted_edges_from(edges_LSM1c)
PCCc.add_weighted_edges_from(edges_PCCc)



for i in grafitos_c:
    print(i)
    print('Degree connectivity', nx.degree(i))

#%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%


LHIPPc.add_weighted_edges_from(edges_LHIPPc) #adds the edges
widths = nx.get_edge_attributes(LHIPPc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LHIPPc)
nx.draw_networkx_nodes(LHIPPc,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(LHIPPc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LHIPPc, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

mPFCc.add_weighted_edges_from(edges_mPFCc) #adds the edges
widths = nx.get_edge_attributes(mPFCc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mPFCc)
nx.draw_networkx_nodes(mPFCc,pos,
                       node_size=700,
                       node_color='tomato',
                       alpha=0.7)
nx.draw_networkx_edges(mPFCc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mPFCc, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

LSM1c.add_weighted_edges_from(edges_LSM1c) #adds the edges
widths = nx.get_edge_attributes(LSM1c, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LSM1c)
nx.draw_networkx_nodes(LSM1c,pos,
                       node_size=700,
                       node_color='plum',
                       alpha=0.7)
nx.draw_networkx_edges(LSM1c,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LSM1c, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

PCCc.add_weighted_edges_from(edges_PCCc) #adds the edges
widths = nx.get_edge_attributes(PCCc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(PCCc)
nx.draw_networkx_nodes(PCCc,pos,
                       node_size=700,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(PCCc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(PCCc, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTRAREGIONAL NETWORKS PATIENTS 
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

MultiG = nx.MultiGraph()


LHIPPp = nx.Graph()
mPFCp = nx.Graph()
LSM1p = nx.Graph()
PCCp = nx.Graph()


# edges = Significant correlation controlling for local GM (for now wo mcc)

grafitos_p = [LHIPPp, mPFCp, LSM1p, PCCp]

for i in grafitos_p:

    i.add_node('GABA+', color = 'red')
    i.add_node('Glx', color = 'green')
    i.add_node('Glu', color = 'darkgreen')
    i.add_node('Gln', color = 'lightgreen')
    i.add_node('GSH', color = 'blue')
    i.add_node('mI', color = 'magenta')
    i.add_node('tNAA', color = 'yellow')
    i.add_node('tCho', color = 'green')
    i.add_node('tCr', color = 'purple')
    i.add_node('tLac', color = 'pink')


edges_LHIPPp = [('mI','tCr',.613),('tNAA','tCr',.701),
               ('tCho','tCr',.662)] #mcc

edges_mPFCp = [('Glx','Glu',.917)] #mcc

edges_LSM1p = [('Glx','Glu',.880),('Glx','Gln',.873)] #mcc

edges_PCCp = [('GABA+','Glx',.659),('GABA+','Glu',.763),
              ('Glx','Glu',.945),('Glx','Gln',.825),('Glx','mI',.735),
              ('Glu','Gln',.638),('Glu','mI',.633),
              ('Gln','mI',.650),('tNAA','tCr',.699)] #mcc



LHIPPp.add_weighted_edges_from(edges_LHIPPp)
mPFCp.add_weighted_edges_from(edges_mPFCp)
LSM1p.add_weighted_edges_from(edges_LSM1p)
PCCp.add_weighted_edges_from(edges_PCCp)



for i in grafitos_p:
    print(i)
    print('Degree connectivity', nx.degree(i))

#%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%


LHIPPp.add_weighted_edges_from(edges_LHIPPp) #adds the edges
widths = nx.get_edge_attributes(LHIPPp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LHIPPp)
nx.draw_networkx_nodes(LHIPPp,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(LHIPPp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LHIPPp, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

mPFCp.add_weighted_edges_from(edges_mPFCp) #adds the edges
widths = nx.get_edge_attributes(mPFCp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mPFCp)
nx.draw_networkx_nodes(mPFCp,pos,
                       node_size=700,
                       node_color='tomato',
                       alpha=0.7)
nx.draw_networkx_edges(mPFCp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mPFCp, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

LSM1p.add_weighted_edges_from(edges_LSM1p) #adds the edges
widths = nx.get_edge_attributes(LSM1p, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(LSM1p)
nx.draw_networkx_nodes(LSM1p,pos,
                       node_size=700,
                       node_color='plum',
                       alpha=0.7)
nx.draw_networkx_edges(LSM1p,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(LSM1p, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#%^%^%^%^%^%%^%%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%

PCCp.add_weighted_edges_from(edges_PCCp) #adds the edges
widths = nx.get_edge_attributes(PCCp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(PCCp)
nx.draw_networkx_nodes(PCCp,pos,
                       node_size=700,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(PCCp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(PCCp, pos=pos,
                        font_color='black',
                        font_size=16)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()



#^*^*^^*^^*^*^*^*^*^*^^**^^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^**
#^%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTERREGIONAL NETWORKS FULL SAMPLE 
#^%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&%^&
#^*^*^^*^^*^*^*^*^*^*^^**^^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^**

#to be adapted
MultiG = nx.Graph()

GABA = nx.Graph()
Glx = nx.Graph()
Glu = nx.Graph()
Gln = nx.Graph()
GSH = nx.Graph()
mI = nx.Graph()
NAA = nx.Graph()
Cho = nx.Graph()
Cr = nx.Graph()
Lac = nx.Graph()


grafos = [GABA,Glx,Glu,Gln,GSH,mI,NAA,Cho,Cr,Lac]

for i in grafos:

    i.add_node('LHIPP', color = 'red')
    i.add_node('mPFC', color = 'green')
    i.add_node('LSM1', color = 'darkgreen')
    i.add_node('PCC', color = 'lightgreen')


edges_GABA =[('mPFC','LSM1',.456)] #mcc


edges_Glx = []

edges_Glu = []

edges_Gln = []

edges_GSH = [] #Mcc

edges_mI = [('LHIPP','LSM1',.434),('LHIPP','PCC',.507),('mPFC','LSM1',.441),
            ('mPFC','PCC',.495),('LSM1','PCC',.698)] #mcc

edges_NAA = [('LSM1','mPFC',.424),('LSM1','PCC',.402)] #mcc

edges_Cho = []

edges_Cr = [('LHIPP','LSM1',.423),('mPFC','LSM1',.572),('mPFC','PCC',.382),
            ('PCC','LSM1',.368)] #mcc

edges_Lac = [] #mcc


for i in grafos:
    print(i)
    print('Degree connectivity', nx.degree(i))



nx.draw(GABA, with_labels=1)
nx.draw(Glx, with_labels=1)
nx.draw(Glu, with_labels=1)
nx.draw(Gln, with_labels=1)
nx.draw(GSH, with_labels=1)
nx.draw(mI, with_labels=1)
nx.draw(NAA, with_labels=1)
nx.draw(Cho, with_labels=1)
nx.draw(Cr, with_labels=1)
nx.draw(Lac, with_labels=1)


GABA.add_weighted_edges_from(edges_GABA) #adds the edges
widths = nx.get_edge_attributes(GABA, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(GABA)
nx.draw_networkx_nodes(GABA,pos,
                       node_size=700,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(GABA,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(GABA, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glx.add_weighted_edges_from(edges_Glx) #adds the edges
widths = nx.get_edge_attributes(Glx, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Glx)
nx.draw_networkx_nodes(Glx,pos,
                       node_size=700,
                       node_color='blue',
                       alpha=0.7)
nx.draw_networkx_edges(Glx,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='blue',
                       alpha=0.6)
nx.draw_networkx_labels(Glx, pos=pos,
                        font_color='black',
                        font_size=20)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glu.add_weighted_edges_from(edges_Glu) #adds the edges
widths = nx.get_edge_attributes(Glu, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Glu)
nx.draw_networkx_nodes(Glu,pos,
                       node_size=700,
                       node_color='cyan',
                       alpha=0.7)
nx.draw_networkx_edges(Glu,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Glu, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Gln.add_weighted_edges_from(edges_Gln) #adds the edges
widths = nx.get_edge_attributes(Gln, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Gln)
nx.draw_networkx_nodes(Gln,pos,
                       node_size=700,
                       node_color='lightseagreen',
                       alpha=0.7)
nx.draw_networkx_edges(Gln,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Gln, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


GSH.add_weighted_edges_from(edges_GSH) #adds the edges
widths = nx.get_edge_attributes(GSH, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(GSH)
nx.draw_networkx_nodes(GSH,pos,
                       node_size=700,
                       node_color='gold',
                       alpha=0.7)
nx.draw_networkx_edges(GSH,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(GSH, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&



mI.add_weighted_edges_from(edges_mI) #adds the edges
widths = nx.get_edge_attributes(mI, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mI)
nx.draw_networkx_nodes(mI,pos,
                       node_size=700,
                       node_color='violet',
                       alpha=0.7)
nx.draw_networkx_edges(mI,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mI, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


NAA.add_weighted_edges_from(edges_NAA) #adds the edges
widths = nx.get_edge_attributes(NAA, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(NAA)
nx.draw_networkx_nodes(NAA,pos,
                       node_size=700,
                       node_color='khaki',
                       alpha=0.7)
nx.draw_networkx_edges(NAA,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(NAA, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Cho.add_weighted_edges_from(edges_Cho) #adds the edges
widths = nx.get_edge_attributes(Cho, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Cho)
nx.draw_networkx_nodes(Cho,pos,
                       node_size=700,
                       node_color='paleturquoise',
                       alpha=0.7)
nx.draw_networkx_edges(Cho,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Cho, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Cr.add_weighted_edges_from(edges_Cr) #adds the edges
widths = nx.get_edge_attributes(Cr, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Cr)
nx.draw_networkx_nodes(Cr,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(Cr,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Cr, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Lac.add_weighted_edges_from(edges_Lac) #adds the edges
widths = nx.get_edge_attributes(Lac, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Lac)
nx.draw_networkx_nodes(Lac,pos,
                       node_size=700,
                       node_color='mediumvioletred',
                       alpha=0.7)
nx.draw_networkx_edges(Lac,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Lac, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#%^&%^&%^%&*%^&*%^&*%^*%^&*%^&*%^&*%^&*%^&*%^&*%^&*%^*%^*%^&*%^*%^&*%^*%^&*
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTERREGIONAL NETWORKS CONTROLS
#%^&%^&%^%&*%^&*%^&*%^*%^&*%^&*%^&*%^&*%^&*%^&*%^&*%^*%^*%^&*%^*%^&*%^*%^&*

MultiG = nx.Graph()

GABAc = nx.Graph()
Glxc = nx.Graph()
Gluc = nx.Graph()
Glnc = nx.Graph()
GSHc = nx.Graph()
mIc = nx.Graph()
NAAc = nx.Graph()
Choc = nx.Graph()
Crc = nx.Graph()
Lacc = nx.Graph()


grafosc = [GABAc,Glxc,Gluc,Glnc,GSHc,mIc,NAAc,Choc,Crc,Lacc]


for i in grafosc:

    i.add_node('LHIPP', color = 'red')
    i.add_node('mPFC', color = 'green')
    i.add_node('LSM1', color = 'darkgreen')
    i.add_node('PCC', color = 'lightgreen')



edges_GABAc =[]

edges_Glxc = []

edges_Gluc = []

edges_Glnc = []

edges_GSHc = []

edges_mIc = [('LHIPP','PCC',.615),('LSM1','mPFC',.623),('mPFC','PCC',.61)]#mcc

edges_NAAc = []

edges_Choc = [('LHIPP','mPFC',.612)] #mcc

edges_Crc = [('LSM1','mPFC',.781),('PCC','mPFC',.56),
             ('PCC','LSM1',.51)] #mcc

edges_Lacc = []


for i in grafosc:
    print(i)
    print('Degree connectivity', nx.degree(i))



nx.draw(GABAc, with_labels=1)
nx.draw(Glxc, with_labels=1)
nx.draw(Gluc, with_labels=1)
nx.draw(Glnc, with_labels=1)
nx.draw(GSHc, with_labels=1)
nx.draw(mIc, with_labels=1)
nx.draw(NAAc, with_labels=1)
nx.draw(Choc, with_labels=1)
nx.draw(Crc, with_labels=1)
nx.draw(Lacc, with_labels=1)


GABAc.add_weighted_edges_from(edges_GABAc) #adds the edges
widths = nx.get_edge_attributes(GABAc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(GABAc)
nx.draw_networkx_nodes(GABAc,pos,
                       node_size=700,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(GABAc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(GABAc, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glxc.add_weighted_edges_from(edges_Glxc) #adds the edges
widths = nx.get_edge_attributes(Glxc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Glxc)
nx.draw_networkx_nodes(Glxc,pos,
                       node_size=700,
                       node_color='blue',
                       alpha=0.7)
nx.draw_networkx_edges(Glxc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Glxc, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Gluc.add_weighted_edges_from(edges_Gluc) #adds the edges
widths = nx.get_edge_attributes(Gluc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Gluc)
nx.draw_networkx_nodes(Gluc,pos,
                       node_size=1500,
                       node_color='cyan',
                       alpha=0.7)
nx.draw_networkx_edges(Gluc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Gluc, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glnc.add_weighted_edges_from(edges_Glnc) #adds the edges
widths = nx.get_edge_attributes(Glnc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Glnc)
nx.draw_networkx_nodes(Glnc,pos,
                       node_size=1500,
                       node_color='lightseagreen',
                       alpha=0.7)
nx.draw_networkx_edges(Glnc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Glnc, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


GSHc.add_weighted_edges_from(edges_GSHc) #adds the edges
widths = nx.get_edge_attributes(GSHc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(GSHc)
nx.draw_networkx_nodes(GSHc,pos,
                       node_size=1500,
                       node_color='gold',
                       alpha=0.7)
nx.draw_networkx_edges(GSHc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(GSHc, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&



mIc.add_weighted_edges_from(edges_mIc) #adds the edges
widths = nx.get_edge_attributes(mIc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mIc)
nx.draw_networkx_nodes(mIc,pos,
                       node_size=700,
                       node_color='violet',
                       alpha=0.7)
nx.draw_networkx_edges(mIc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mIc, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


NAAc.add_weighted_edges_from(edges_NAAc) #adds the edges
widths = nx.get_edge_attributes(NAAc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(NAAc)
nx.draw_networkx_nodes(NAAc,pos,
                       node_size=700,
                       node_color='khaki',
                       alpha=0.7)
nx.draw_networkx_edges(NAAc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(NAAc, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Choc.add_weighted_edges_from(edges_Choc) #adds the edges
widths = nx.get_edge_attributes(Choc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Choc)
nx.draw_networkx_nodes(Choc,pos,
                       node_size=700,
                       node_color='paleturquoise',
                       alpha=0.7)
nx.draw_networkx_edges(Choc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Choc, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Crc.add_weighted_edges_from(edges_Crc) #adds the edges
widths = nx.get_edge_attributes(Crc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Crc)
nx.draw_networkx_nodes(Crc,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(Crc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Crc, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Lacc.add_weighted_edges_from(edges_Lacc) #adds the edges
widths = nx.get_edge_attributes(Lacc, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Lacc)
nx.draw_networkx_nodes(Lacc,pos,
                       node_size=700,
                       node_color='mediumvioletred',
                       alpha=0.7)
nx.draw_networkx_edges(Lacc,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Lacc, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/* INTERREGIONAL NETWORKS PATIENTS
#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*#/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

MultiG = nx.Graph()

GABAp = nx.Graph()
Glxp = nx.Graph()
Glup = nx.Graph()
Glnp = nx.Graph()
GSHp = nx.Graph()
mIp = nx.Graph()
NAAp = nx.Graph()
Chop = nx.Graph()
Crp = nx.Graph()
Lacp = nx.Graph()

grafosp = [GABAp,Glxp,Glup,Glnp,GSHp,mIp,NAAp,Chop,Crp,Lacp]


for i in grafosp:
    i.add_node('LHIPP', color = 'red')
    i.add_node('mPFC', color = 'green')
    i.add_node('LSM1', color = 'darkgreen')
    i.add_node('PCC', color = 'lightgreen')

edges_GABAp =[]


edges_Glxp = []

edges_Glup = []

edges_Glnp = []

edges_GSHp = []

edges_mIp = [('LHIPP','PCC',.544),('LSM1','PCC',.698)] #mcc

edges_NAAp = [('mPFC','LSM1',.563),('LSM1','PCC',.402)] #mcc

edges_Chop = []

edges_Crp = [('LHIPP','LSM1',.51),('LHIPP','PCC',.615)]

edges_Lacp = []


for i in grafosp:
    print(i)
    print('Degree connectivity', nx.degree(i))



nx.draw(GABAp, with_labels=1)
nx.draw(Glxp, with_labels=1)
nx.draw(Glup, with_labels=1)
nx.draw(Glnp, with_labels=1)
nx.draw(GSHp, with_labels=1)
nx.draw(mIp, with_labels=1)
nx.draw(NAAp, with_labels=1)
nx.draw(Chop, with_labels=1)
nx.draw(Crp, with_labels=1)
nx.draw(Lacp, with_labels=1)


GABAp.add_weighted_edges_from(edges_GABAp) #adds the edges
widths = nx.get_edge_attributes(GABAp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(GABAp)
nx.draw_networkx_nodes(GABAp,pos,
                       node_size=1500,
                       node_color='yellow',
                       alpha=0.7)
nx.draw_networkx_edges(GABAp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(GABAp, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glxp.add_weighted_edges_from(edges_Glxp) #adds the edges
widths = nx.get_edge_attributes(Glxp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Glxp)
nx.draw_networkx_nodes(Glxp,pos,
                       node_size=1500,
                       node_color='blue',
                       alpha=0.7)
nx.draw_networkx_edges(Glxp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Glxp, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glup.add_weighted_edges_from(edges_Glup) #adds the edges
widths = nx.get_edge_attributes(Glup, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Glup)
nx.draw_networkx_nodes(Glup,pos,
                       node_size=1500,
                       node_color='cyan',
                       alpha=0.7)
nx.draw_networkx_edges(Glup,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Glup, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Glnp.add_weighted_edges_from(edges_Glnp) #adds the edges
widths = nx.get_edge_attributes(Glnp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Glnp)
nx.draw_networkx_nodes(Glnp,pos,
                       node_size=1500,
                       node_color='lightseagreen',
                       alpha=0.7)
nx.draw_networkx_edges(Glnp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Glnp, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()


#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


GSHp.add_weighted_edges_from(edges_GSHp) #adds the edges
widths = nx.get_edge_attributes(GSHp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(GSHp)
nx.draw_networkx_nodes(GSHp,pos,
                       node_size=1500,
                       node_color='gold',
                       alpha=0.7)
nx.draw_networkx_edges(GSHp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(GSHp, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&



mIp.add_weighted_edges_from(edges_mIp) #adds the edges
widths = nx.get_edge_attributes(mIp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(mIp)
nx.draw_networkx_nodes(mIp,pos,
                       node_size=700,
                       node_color='violet',
                       alpha=0.7)
nx.draw_networkx_edges(mIp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(mIp, pos=pos,
                        font_color='black',
                        font_size=19
                        )

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


NAAp.add_weighted_edges_from(edges_NAAp) #adds the edges
widths = nx.get_edge_attributes(NAAp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(NAAp)
nx.draw_networkx_nodes(NAAp,pos,
                       node_size=700,
                       node_color='khaki',
                       alpha=0.7)
nx.draw_networkx_edges(NAAp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(NAAp, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Chop.add_weighted_edges_from(edges_Chop) #adds the edges
widths = nx.get_edge_attributes(Chop, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Chop)
nx.draw_networkx_nodes(Chop,pos,
                       node_size=700,
                       node_color='paleturquoise',
                       alpha=0.7)
nx.draw_networkx_edges(Chop,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Chop, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Crp.add_weighted_edges_from(edges_Crp) #adds the edges
widths = nx.get_edge_attributes(Crp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 8)
pos = nx.shell_layout(Crp)
nx.draw_networkx_nodes(Crp,pos,
                       node_size=700,
                       node_color='lightgreen',
                       alpha=0.7)
nx.draw_networkx_edges(Crp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='black',
                       alpha=0.6)
nx.draw_networkx_labels(Crp, pos=pos,
                        font_color='black',
                        font_size=19)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()

#^&^&^&^&^&^^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&


Lacp.add_weighted_edges_from(edges_Lacp) #adds the edges
widths = nx.get_edge_attributes(Lacp, 'weight')
width=list(widths.values())
widthx=[]

for element in width:
    widthx.append(element * 15)
pos = nx.shell_layout(Lacp)
nx.draw_networkx_nodes(Lacp,pos,
                       node_size=1500,
                       node_color='mediumvioletred',
                       alpha=0.7)
nx.draw_networkx_edges(Lacp,pos,
                       edgelist = widths.keys(),
                       width=widthx,
                       edge_color='skyblue',
                       alpha=0.6)
nx.draw_networkx_labels(Lacp, pos=pos,
                        font_color='black',
                        font_size=14)

plt.axis('off')
axis = plt.gca()
axis.set_xlim([1.*x for x in axis.get_xlim()])
axis.set_ylim([1.*y for y in axis.get_ylim()])
plt.tight_layout()
plt.box(False)
plt.show()
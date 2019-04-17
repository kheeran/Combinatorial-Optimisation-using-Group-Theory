import numpy as np
import time as time
import pickle
import networkx as nx
import plotly.plotly as py
from plotly.graph_objs import *

# Reference: https://plot.ly/python/igraph-networkx-comparison/#networkx

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 0)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


visited = load_obj("visited")
vertices = list(visited.keys())
edges = [(p,visited[p][0]) for p in vertices]

# Removing the initial node to itself
index = edges.index(('0123456700000000', ''))
edges.pop(index)

print (vertices)

N = len(vertices)
V = range(N)
E = edges

g=nx.Graph()
g.add_nodes_from(V)
g.add_edges_from(E)

pos=nx.fruchterman_reingold_layout(g)

Xv=[pos[k][0] for k in range(N)]
Yv=[pos[k][1] for k in range(N)]
Xed=[]
Yed=[]
for edge in E:
    Xed+=[pos[edge[0]][0],pos[edge[1]][0], None]
    Yed+=[pos[edge[0]][1],pos[edge[1]][1], None]

trace3=Scatter(x=Xed,
               y=Yed,
               mode='lines',
               line=dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace4=Scatter(x=Xv,
               y=Yv,
               mode='markers',
               name='net',
               marker=dict(symbol='circle-dot',
                             size=5,
                             color='#6959CD',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               text=vertices,
               hoverinfo='text'
               )

annot="This networkx.Graph has the Fruchterman-Reingold layout<br>Code:"+\
"<a href='http://nbviewer.ipython.org/gist/empet/07ea33b2e4e0b84193bd'> [2]</a>"

data1=[trace3]
fig1=Figure(data=data1, layout=Layout(title="First Plot"))
# fig1['layout']['annotations'][0]['text']=annot
py.iplot(fig1, filename='Coautorship-network-nx')

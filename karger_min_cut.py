# -*- coding: utf-8 -*-

import numpy as np

with open('kargerMinCut.txt', 'r') as f:
    graph = f.read()

graph = graph.split('\n')[:-1]

graph_dict = {}
for vertex in graph:
    vertex = vertex.split('\t')[:-1]
    graph_dict[vertex[0]] = set(vertex[1:]) 
    

np.random.choice(list(graph_dict.keys()), size = 2)
graph_dict.keys()

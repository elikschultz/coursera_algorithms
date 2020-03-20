# -*- coding: utf-8 -*-

import numpy as np

# Read in file
with open('kargerMinCut.txt', 'r') as f:
    graph = f.read()

graph = graph.split('\n')[:-1]

# Represent adjacency list as dictionary and create list of edges
graph_dict = {}
edges = []
for vertex in graph:
    vertex = vertex.split('\t')[:-1]
    graph_dict[vertex[0]] = vertex[1:]
    edges_to_add = ((x, y) for x in [vertex[0]] for y in vertex[1:])
    for edge in edges_to_add:
        if [edge[0] < edge[1]]:
            edges.append(edge)
    
# Create list to track number of crossing edges for each pass of algorithm
crossing_edges = 200*199/2

for i in range(100000):
    np.random.shuffle(edges)
    nodes = set()
    node_dict = dict(zip([str(x) for x in range(1, 201)], [set([str(x)]) for x in range(1, 201)]))
    for edge in edges:
        if len(node_dict[edge[0]].union(node_dict[edge[1]])) == 200:
            if len(node_dict[edge[0]]) > len(node_dict[edge[1]]):
                crossing_edges_new = 0
                for i in list(node_dict[edge[1]]):
                    crossing_edges_new += len(set(graph_dict[i]).difference(node_dict[edge[1]]))
                
                if crossing_edges > crossing_edges_new:
                    crossing_edges = crossing_edges_new
                    
            else:
                crossing_edges_new = 0
                for i in list(node_dict[edge[0]]):
                    crossing_edges_new += len(set(graph_dict[i]).difference(node_dict[edge[0]]))
                
                if crossing_edges > crossing_edges_new:
                    crossing_edges = crossing_edges_new

            break
        elif node_dict[edge[0]] == node_dict[edge[1]]:
            continue
        else:
            node_dict[edge[0]].update(node_dict[edge[1]])
            for i in node_dict[edge[1]]:
                node_dict[i] = node_dict[edge[0]]
            node_dict[edge[1]] = node_dict[edge[0]]   
print(crossing_edges)
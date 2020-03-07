# -*- coding: utf-8 -*-

import numpy as np
import copy
import time

# Read in file
with open('kargerMinCut.txt', 'r') as f:
    graph = f.read()

graph = graph.split('\n')[:-1]

# Represent adjacency list as dictionary of nodes, where each entry consists of another
# dictionary with keys corresponding to adjacent nodes and values corresponding to 
# number of edges connecting the two
graph_dict = {}
for vertex in graph:
    vertex = vertex.split('\t')[:-1]
    graph_dict[vertex[0]] = {}
    for connected_vertex in vertex[1:]:
        graph_dict[vertex[0]][connected_vertex] = 1

# Create list to track number of crossing edges for each pass of algorithm
crossing_edges = 200*199/2

t1 = time.time()
# Run algorithm 100000 times
for i in range(100000):
    graph_dict_copy = copy.deepcopy(graph_dict)
    while len(graph_dict_copy.keys()) > 2: 
        # Choose two nodes to combine at random
        to_combine_0 = np.random.choice(list(graph_dict_copy.keys()), size = 1)[0]
        to_combine_1 = np.random.choice(list(graph_dict_copy[to_combine_0].keys()), 
                                        size = 1)[0]
        
        # Add new key to adjacency list representing merged node and get adjacent nodes/counts of 
        # connecting edges; remove old nodes that are now merged; update nodes that
        # were not involved in the merge to reflect the merge
        new_node = to_combine_0 + ", " + to_combine_1
        graph_dict_copy[new_node] = {}
        
        for adj_node in graph_dict_copy[to_combine_0].keys():
            if adj_node != to_combine_1:
                graph_dict_copy[new_node][adj_node] = graph_dict_copy[to_combine_0][adj_node]
                graph_dict_copy[adj_node][new_node] = graph_dict_copy[adj_node][to_combine_0]
            del graph_dict_copy[adj_node][to_combine_0]
        
        for adj_node in graph_dict_copy[to_combine_1].keys():
            if adj_node != to_combine_0:
                graph_dict_copy[new_node][adj_node] = graph_dict_copy[new_node].get(adj_node, 0) + \
                    graph_dict_copy[to_combine_1][adj_node]
                graph_dict_copy[adj_node][new_node] = graph_dict_copy[adj_node].get(new_node, 0) + \
                    graph_dict_copy[adj_node][to_combine_1]
            del graph_dict_copy[adj_node][to_combine_1]
                
        del graph_dict_copy[to_combine_0]
        del graph_dict_copy[to_combine_1]
        
        final_node_1 = new_node
        final_node_2 = list(graph_dict_copy[new_node].keys())[0]

    if graph_dict_copy[final_node_1][final_node_2] < crossing_edges:
        crossing_edges = graph_dict_copy[final_node_1][final_node_2]
print(time.time() - t1)
# -*- coding: utf-8 -*-

import numpy as np

# Read in file
with open('kargerMinCut.txt', 'r') as f:
    graph = f.read()

graph = graph.split('\n')[:-1]

# Create list to track number of crossing edges for each pass of algorithm
crossing_edges = []

# Run algorithm 1000 times
for i in range(1000): 
    # Represent adjacency list as dictionary of nodes, where each entry consists of another
    # dictionary with keys corresponding to adjacent nodes and values corresponding to 
    # number of edges connecting the two
    graph_dict = {}
    for vertex in graph:
        vertex = vertex.split('\t')[:-1]
        graph_dict[vertex[0]] = {}
        for connected_vertex in vertex[1:]:
            graph_dict[vertex[0]][connected_vertex] = 1
    
    final_node_1= ''
    final_node_2 = ''
    while len(graph_dict.keys()) > 2: 
        # Choose two nodes to combine at random
        to_combine = np.random.choice(list(graph_dict.keys()), size = 2, replace = False)
        
        # Add new key to adjacency list representing merged node and get adjacent nodes/counts of 
        # connecting edges
        new_node = to_combine[0] + ", " + to_combine[1]
        graph_dict[new_node] = {}
        for adj_node in graph_dict[to_combine[0]].keys():
            if adj_node != to_combine[1]:
                graph_dict[new_node][adj_node] = graph_dict[to_combine[0]][adj_node]
        for adj_node in graph_dict[to_combine[1]].keys():
            if adj_node != to_combine[0]:
                graph_dict[new_node][adj_node] = graph_dict[new_node].get(adj_node, 0) + \
                    graph_dict[to_combine[1]][adj_node]
    
        # Replace all references to the two nodes that were merged with references to the new node
        for node in graph_dict.keys():
            if to_combine[0] in graph_dict[node].keys():
                graph_dict[node][new_node] = graph_dict[node][to_combine[0]]
                del graph_dict[node][to_combine[0]]
                
            if to_combine[1] in graph_dict[node].keys():
                graph_dict[node][new_node] = graph_dict[node].get(new_node, 0) + \
                    graph_dict[node][to_combine[1]]
                del graph_dict[node][to_combine[1]]
                
        del graph_dict[to_combine[0]]
        del graph_dict[to_combine[1]]
        
        final_node_1 = new_node
        final_node_2 = list(graph_dict[new_node].keys())[0]

    crossing_edges.append(graph_dict[final_node_1][final_node_2])
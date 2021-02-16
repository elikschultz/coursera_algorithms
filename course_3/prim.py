# -*- coding: utf-8 -*-

with open('edges.txt', 'r') as f:
    edges = [(int(i.split()[0]), int(i.split()[1]), int(i.split()[2])) for i in f.read().split('\n')[1:-1]]

# Create adjacency list representation of graph
graph_dict = {}
for edge in edges:
    graph_dict[edge[0]] = graph_dict.get(edge[0], {})
    graph_dict[edge[0]].update({edge[1]: edge[2]})
    
    graph_dict[edge[1]] = graph_dict.get(edge[1], {})
    graph_dict[edge[1]].update({edge[0]: edge[2]})

# Initialize values to be used in executing Prim's algorithm    
mst_edges = []
mst_cost = 0
node_costs = dict(zip(range(2, len(graph_dict) + 1), [float('inf')] * (len(graph_dict) - 1)))
next_node = 1

# Perform Prim's algorithm
while len(mst_edges) < len(graph_dict) - 1:
    for key in graph_dict[next_node].keys():
        if key in node_costs.keys():
            if graph_dict[next_node][key] < node_costs[key]:
                node_costs[key] = graph_dict[next_node][key]
     
    mst_edges.append((next_node, min(node_costs, key = node_costs.get), node_costs.pop(min(node_costs, key = node_costs.get))))
    mst_cost += mst_edges[-1][2]
    next_node = mst_edges[-1][1]

print(mst_cost)
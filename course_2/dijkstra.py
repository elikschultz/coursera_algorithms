# -*- coding: utf-8 -*-

# Read in data and create graph
with open('dijkstraData.txt', 'r') as f:
    dijkstra_data = f.read()
    
dijkstra_data = [row.split('\t')[:-1] for row in dijkstra_data.split('\n')[:-1]]
dijkstra_graph = {}
for row in dijkstra_data:
    dijkstra_graph[int(row[0])] = dict([[int(x) for x in edge.split(',')] for edge in row[1:]])
    
def dijkstra_search(start_node, graph):
    nodes_visited = {start_node: 0}
    candidate_nodes = graph[start_node].copy()
    # Add unvisited nodes one by one based on minimum Dijkstra distance
    for i in range(len(graph.keys()) - 1):
        node_to_add = min(candidate_nodes, key = candidate_nodes.get)
        nodes_visited[node_to_add] = candidate_nodes.pop(node_to_add)
        for node_to_check in graph[node_to_add].keys():
            if node_to_check not in nodes_visited.keys():
                candidate_nodes[node_to_check] = min(candidate_nodes.get(node_to_check, float('inf')), graph[node_to_add][node_to_check] + nodes_visited[node_to_add])
    
    return(nodes_visited)

",".join([str(dijkstra_search(1, dijkstra_graph)[i]) for i in [7,37,59,82,99,115,133,165,188,197]])

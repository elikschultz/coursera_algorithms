# -*- coding: utf-8 -*-

# Read in file and create graph
class Graph:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            edges = file.read()
            
        edges = [edge.strip().split(' ') for edge in edges.split('\n')]
        
        self.nodes = {}
        
        for edge in edges:
            node1 = self.nodes.get(edge[0], {'incoming': [],
                             'outgoing': [],
                             'visited': False,
                             'leader': None,
                             'visit_order': None})
            node1['outgoing'].append(edge[1])
            self.nodes[edge[0]] = node1
            
            node2 = self.nodes.get(edge[1], {'incoming': [],
                             'outgoing': [],
                             'visited': False,
                             'leader': None,
                             'visit_order': None})
            node2['incoming'].append(edge[0])
            self.nodes[edge[1]] = node2
        
        self.n = 1
        self.stack = []
        
    def __str__(self):
       return str(self.nodes)
            
    def dfs(self, direction = 'outgoing'):
        for node in self.nodes.keys():
            if self.nodes[node]['visited'] == False:
                self.nodes[node]['visited'] = True
                self.stack.append(node)
                for next_node in self.nodes[node][direction]:
                    if self.nodes[next_node]['visited'] == False:
                        self.nodes[next_node]['visited'] = True
                        self.stack.append(next_node)
                while len(self.stack) != 0:
                    nodes_to_add = []
                    for potential_node_to_add in self.nodes[self.stack[-1]][direction]:
                        if self.nodes[potential_node_to_add]['visited'] == False:
                            self.nodes[potential_node_to_add]['visited'] = True
                            nodes_to_add.append(potential_node_to_add)
                    if len(nodes_to_add) == 0:
                        next_node_visited = self.stack.pop()
                        self.nodes[next_node_visited]['visit_order'] = self.n
                        self.n += 1
                    else:
                        self.stack.extend(nodes_to_add)
                
    def reset(self):
        for node in self.nodes.keys():
            self.nodes[node]['visited'] = False
            self.nodes[node]['leader'] = None
            self.nodes[node]['visit_order'] = None
        self.n = 1
            
scc_graph = Graph('SCC.txt')        

x = [scc_graph.nodes[node]['visit_order'] for node in scc_graph.nodes.keys()]
        
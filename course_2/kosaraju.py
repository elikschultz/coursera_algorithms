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
        self.node_order = self.nodes.keys()
        
    def __str__(self):
       return str(self.nodes)
            
    def dfs(self, direction = 'outgoing'):
        new_node_order = []
        for node in self.node_order:
            if self.nodes[node]['visited'] == False:
                self.nodes[node]['visited'] = True
                self.nodes[node]['leader'] = node
                self.stack.append(node)
                current_leader = node
                for next_node in self.nodes[node][direction]:
                    if self.nodes[next_node]['visited'] == False:
                        self.nodes[next_node]['visited'] = True
                        self.nodes[next_node]['leader'] = current_leader
                        self.stack.append(next_node)
                while len(self.stack) != 0:
                    nodes_to_add = []
                    for potential_node_to_add in self.nodes[self.stack[-1]][direction]:
                        if self.nodes[potential_node_to_add]['visited'] == False:
                            self.nodes[potential_node_to_add]['visited'] = True
                            self.nodes[potential_node_to_add]['leader'] = current_leader
                            nodes_to_add.append(potential_node_to_add)
                    if len(nodes_to_add) == 0:
                        next_node_visited = self.stack.pop()
                        self.nodes[next_node_visited]['visit_order'] = self.n
                        self.n += 1
                        new_node_order.append(next_node_visited)
                    else:
                        self.stack.extend(nodes_to_add)
        new_node_order.reverse()
        self.node_order = new_node_order
          
    def soft_reset(self):
        for node in self.nodes.keys():
            self.nodes[node]['visited'] = False
            self.nodes[node]['leader'] = None
            self.nodes[node]['visit_order'] = None
        self.n = 1
            
    def hard_reset(self):
        for node in self.nodes.keys():
            self.nodes[node]['visited'] = False
            self.nodes[node]['leader'] = None
            self.nodes[node]['visit_order'] = None
        self.n = 1
        self.node_order = self.nodes.keys()
        
    def compute_scc_sizes(self):
        result = {}
        for node in self.nodes.keys():
            result[self.nodes[node]['leader']] = result.get(self.nodes[node]['leader'], 0) + 1
        return(result)
            
scc_graph = Graph('SCC.txt')
scc_graph.dfs('incoming')
scc_graph.soft_reset()
scc_graph.dfs()
print(sorted(scc_graph.compute_scc_sizes().values())[-5:])
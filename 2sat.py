# Represent 2-SAT problem as directed graph and determine solvability via SCC.

# For every variable in the 2-SAT instance, add two vertices, one for each True/False
# state. Variables are indexed by integers, where positive value indicates variable is 
# true and negative indicating it's false. For each constraint, add an two directed edges 
# (to represent that if one part of constraint is violated, other must be satisfied). 
# The 2-SAT instance will be solvable iff for all vertices v, there is never a case
# where +v and -v are part of the same SCC.

# Read in file and create graph
class Graph_From_2SAT:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.n_variables = int(file.readline())
            edges = []
            while True:
                edge = file.readline()
                
                if not edge:
                    break
                
                edge = edge.split(' ')
                edges.append([-int(edge[0]), int(edge[1])])
                edges.append([-int(edge[1]), int(edge[0])])
        
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
                   
def check_2sat(file_name):
    scc_graph = Graph_From_2SAT(file_name)
    scc_graph.dfs('incoming')
    scc_graph.soft_reset()
    scc_graph.dfs()
    for i in range(1, scc_graph.n_variables + 1):
        if (i in scc_graph.nodes.keys()) and (-i in scc_graph.nodes.keys()):
            if scc_graph.nodes[i]['leader'] == scc_graph.nodes[-i]['leader']:
                return(' '.join(['No feasible solution for 2-SAT instance in', file_name]))
    return(' '.join(['Feasible solution for 2-SAT instance in', file_name]))

for file_to_check in ['2sat1.txt', '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']:
    print(check_2sat(file_to_check))
    
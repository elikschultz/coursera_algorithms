# -*- coding: utf-8 -*-

def floyd_warshall(file_name):
    with open(file_name, 'r') as f:
        n_vertices = int(f.readline().split()[0])
        edges = [[int(j) for j in i.split()] for i in f.read().split('\n')[:-1]]
    
    graph_dict = {}
    for edge in edges:
        graph_dict[edge[0]] = graph_dict.get(edge[0], {})
        graph_dict[edge[0]].update({edge[1]: edge[2]})
    
    # Create array to store solution to subproblems at previous iteeration of k (when 
    # algorithm is at iteration k, this means that only vertices with index less than 
    # or equal to k can be used internally in a path between two nodes i and j)
    A = []
    
    # Initialize for k = 0
    for i in range(n_vertices):
        row_i = []
        for j in range(n_vertices):
            if i == j:
                row_i.append(0)
            else:
                try:
                    row_i.append(graph_dict[i + 1][j + 1])
                except KeyError:
                    row_i.append(float('inf'))
        A.append(row_i)
         
    for k in range(n_vertices):
        # Create array to track i, j shortest paths at iteration k
        B = []
        for i in range(n_vertices):
            row_i = []
            for j in range(n_vertices):
                row_i.append(min(A[i][j], A[i][k] + A[k][j]))
            B.append(row_i)
        A = B
            
    for i in range(n_vertices):
        if A[i][i] < 0:
            return('Negative cycle present.')
    
    return(min([min(i) for i in A]))
    
print('File 1 shortest shortest path:', floyd_warshall('g1.txt'))
print('File 2 shortest shortest path:', floyd_warshall('g2.txt'))
print('File 3 shortest shortest path:', floyd_warshall('g3.txt'))
            
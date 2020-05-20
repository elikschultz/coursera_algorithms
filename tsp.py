# -*- coding: utf-8 -*-
import itertools as it

with open('tsp.txt', 'r') as f:
    n_vertices = int(f.readline())
    vertices = [(float(i.split(' ')[0]), float(i.split(' ')[1])) for i in f.read().split('\n')[:-1]]

def euclidean_dist(tuple_0, tuple_1):
    return(((tuple_0[0] - tuple_1[0])**2 + (tuple_0[1] - tuple_1[1])**2)**(1/2))
    
edges = {}
for i in range(n_vertices):
    for j in range(i):
        edges[(i, j)] = euclidean_dist(vertices[i], vertices[j])
        edges[(j, i)] = euclidean_dist(vertices[i], vertices[j])
    
# Create dictionary of subproblem solutions indexed by subset of vertices used and destination vertex
subproblem_solutions = {}
subproblem_solutions[((0,), 0)] = 0

# Iterate over subproblems
for i in range(1, n_vertices):
    subproblem_solutions[((0,), i)] = float('inf')
    subproblem_solutions[((0, i), i)] = edges[(0, i)]
for i in range(2, n_vertices):
    print(i)
    for s in it.combinations(range(1, n_vertices), i):
        for j in range(1, n_vertices):
            if j in s:
                subproblem_solutions[((0,) + s, j)] = min([subproblem_solutions[(0,) + 
                                    tuple([n for n in s if n != j]), k] + edges[(k, j)] for k in s if k != j])
min([subproblem_solutions[tuple([i for i in range(n_vertices)]), j] + edges[j, 0] for j in range(1, n_vertices)])//1
            
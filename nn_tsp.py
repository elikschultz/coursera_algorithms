# -*- coding: utf-8 -*-
# Read in file
with open('nn.txt') as f:
    n_vertices = int(f.readline())
    vertices = dict()
    next_line = f.readline()
    while next_line != '':
        vertices[int(next_line.split(' ')[0])] = (float(next_line.split(' ')[1]), 
                     float(next_line.split(' ')[2]))
        next_line = f.readline()
        
def sq_dist(tuple_0, tuple_1):
    return (tuple_0[0] - tuple_1[0])**2 + (tuple_0[1] - tuple_1[1])**2

# Implement nearest neighbor heuristic for TSP        
vertices_visited = set([1])
vertices_not_visited = set([i + 1 for i in range(1, n_vertices)])
vertex = 1
tsp_dist = 0
while len(vertices_visited) < n_vertices:
    dist_to_next_vertex = float('inf')
    for candidate in sorted(vertices_not_visited):
        candidate_dist = sq_dist(vertices[vertex], vertices[candidate])
        if candidate_dist < dist_to_next_vertex:
            dist_to_next_vertex = candidate_dist
            next_vertex = candidate
    tsp_dist += dist_to_next_vertex**(1/2)
    vertices_not_visited.discard(next_vertex)
    vertices_visited.add(next_vertex)
    vertex = next_vertex
    
tsp_dist = tsp_dist
tsp_dist += sq_dist(vertices[vertex], vertices[1])**(1/2)

print(tsp_dist//1)
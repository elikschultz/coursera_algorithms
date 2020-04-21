# -*- coding: utf-8 -*-

with open('clustering_big.txt', 'r') as f:
    size_and_n_bits = [int(i) for i in f.readline().split()]
    vertices = [''.join(i.split()) for i in f.read().split('\n')[:-1]]
    
# First, all vertices with Hamming distance zero must be in the same cluster
unique_vertices = set()
for vertex in vertices:
    unique_vertices.add(vertex)
    
# Catalog which cluster a given vertex belongs to
vertices = dict(zip(unique_vertices, unique_vertices))

# Catalog which vertices belong to a given cluster (arbitrary vertex in cluster used as label), as well as the cluster's size
clusters = {}
for vertex in vertices.keys():
    clusters[vertex] = {'size': 1, 'members': [vertex]}   
    
# Next, all vertices with Hamming distance one must be in the same cluster
for i in range(size_and_n_bits[1]):
    patterns = {}
    
    for vertex in unique_vertices:
        if vertex[:i] + '_' + vertex[(i + 1):] not in patterns:
            patterns[vertex[:i] + '_' + vertex[(i + 1):]] = vertex
        else:
            # Write code to check whether vertex and first vertex with given pattern seen belong to same cluster, and if 
            # not combine them
            if vertices[vertex] != vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]]:
                if clusters[vertices[vertex]]['size'] > clusters[vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]]]['size']:
                    to_append = clusters.pop(vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]])
                    clusters[vertices[vertex]]['size'] += to_append['size']
                    clusters[vertices[vertex]]['members'].extend(to_append['members'])
                    
                    for smaller_cluster_vertex in to_append['members']:
                        vertices[smaller_cluster_vertex] = vertices[vertex]
                        
                else:
                    to_append = clusters.pop(vertices[vertex])
                    clusters[vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]]]['size'] += to_append['size']
                    clusters[vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]]]['members'].extend(to_append['members'])
                    
                    for smaller_cluster_vertex in to_append['members']:
                        vertices[smaller_cluster_vertex] = vertices[patterns[vertex[:i] + '_' + vertex[(i + 1):]]]

# Finally, make sure that all vertices with Hamming distance two are in the same cluster
for i in range(size_and_n_bits[1]):
    for j in range(i):
        patterns = {}
        
        for vertex in unique_vertices:
            if vertex[:j] + '_' + vertex[(j + 1):i] + '_' + vertex[(i + 1):] not in patterns:
                patterns[vertex[:j] + '_' + vertex[(j + 1):i] + '_' + vertex[(i + 1):]] = vertex
            else:
                # Write code to check whether vertex and first vertex with given pattern seen belong to same cluster, and if 
                # not combine them
                if vertices[vertex] != vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + '_' + vertex[(i + 1):]]]:
                    if clusters[vertices[vertex]]['size'] > clusters[vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + 
                                                  '_' + vertex[(i + 1):]]]]['size']:
                        to_append = clusters.pop(vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + '_' + vertex[(i + 1):]]])
                        clusters[vertices[vertex]]['size'] += to_append['size']
                        clusters[vertices[vertex]]['members'].extend(to_append['members'])
                    
                        for smaller_cluster_vertex in to_append['members']:
                            vertices[smaller_cluster_vertex] = vertices[vertex]
                            
                    else:
                        to_append = clusters.pop(vertices[vertex])
                        clusters[vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + '_' + 
                                                   vertex[(i + 1):]]]]['size'] += to_append['size']
                        clusters[vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + '_' + 
                                                   vertex[(i + 1):]]]]['members'].extend(to_append['members'])
                        
                        for smaller_cluster_vertex in to_append['members']:
                            vertices[smaller_cluster_vertex] = vertices[patterns[vertex[:j] + '_' + vertex[(j + 1):i] + 
                                                                        '_' + vertex[(i + 1):]]]

print(len(clusters))

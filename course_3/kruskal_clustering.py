# -*- coding: utf-8 -*-

with open('clustering1.txt', 'r') as f:
    file_contents = f.read().split('\n')
    n_vertices = int(file_contents[0])
    edges = [(int(i.split()[0]), int(i.split()[1]), int(i.split()[2])) for i in file_contents[1:-1]]
    
# Adopt merge sort algorithm for sorting edges
def merge_sort(x):
    if len(x) == 1:
        return x
    x_1 = merge_sort(x[:int(len(x)/2)])
    x_2 = merge_sort(x[int(len(x)/2):])
    
    return(merge(x_1, x_2))
    
def merge(x_1, x_2):
    result = []        
    counter_1 = 0
    counter_2 = 0
       
    # Iterate through sorted sublists in parallel, create combined sorted list                
    while counter_1 < len(x_1) and counter_2 < len(x_2):
        if x_1[counter_1][2] < x_2[counter_2][2]:
            result += [x_1[counter_1]]
            counter_1 += 1
            
        else:
            result += [x_2[counter_2]]
            counter_2 += 1
            
    if counter_1 == len(x_1):
        if type(x_2[counter_2:]) == list:
            result += x_2[counter_2:]
        else:
            result += [x_2[counter_2]]
            
    else:
        if type(x_1[counter_1:]) == list:
            result += x_1[counter_1:]
        else:
            result += [x_1[counter_1]]
        
    return(result)

# Create two dictionaries that will be used to perform union-find operations

# Catalog which cluster a given vertex belongs to
vertices = dict(zip(range(1, n_vertices + 1), (range(1, n_vertices + 1))))

# Catalog which vertices belong to a given cluster (arbitrary vertex in cluster used as label), as well as the cluster's size
clusters = {}
for vertex in vertices.keys():
    clusters[vertex] = {'size': 1, 'members': [vertex]}

# Execute Kruskal's algorithm
for edge in merge_sort(edges):
    cluster_0 = vertices[edge[0]]
    cluster_1 = vertices[edge[1]]           
    if len(clusters) > 4:
        if (cluster_0 != cluster_1) and (clusters[cluster_0]['size'] < clusters[cluster_1]['size']):
            cluster_0_info = clusters.pop(cluster_0)
            clusters[cluster_1]['size'] = clusters[cluster_1]['size'] + cluster_0_info['size']
            clusters[cluster_1]['members'].extend(cluster_0_info['members'])
            for vertex in cluster_0_info['members']:
                vertices[vertex] = cluster_1
                
        elif cluster_0 != cluster_1:
            cluster_1_info = clusters.pop(cluster_1)
            clusters[cluster_0]['size'] = clusters[cluster_0]['size'] + cluster_1_info['size']
            clusters[cluster_0]['members'].extend(cluster_1_info['members'])
            for vertex in cluster_1_info['members']:
                vertices[vertex] = cluster_0
                
    elif cluster_0 != cluster_1:
        print('Maximum spacing (in terms of minimal distance between points in different clusters):', edge[2])
        break
    

            
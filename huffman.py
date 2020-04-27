#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('huffman.txt', 'r') as f:
    weights = [int(i) for i in f.read().split('\n')[1:-1]]

class min_heap():
    def __init__(self, array = []):
        self.heap_array = []
        for item in array:
            self.insert(item)
        
    def insert(self, name_weight_tuple):
        self.heap_array.append(name_weight_tuple)
        n = len(self.heap_array)
        
        while n > 1:
            if self.heap_array[n//2 - 1][1] > self.heap_array[n - 1][1]:
                self.heap_array[n//2 - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[n//2 -1]
                n = n//2
            else:
                break
            
    def extract(self):
        if self.heap_array != []:
            self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0]
            return_value = self.heap_array.pop()
            n = 1
            
            while 2*n + 1 <= len(self.heap_array):
                if self.heap_array[2*n - 1][1] < self.heap_array[2*n][1]:
                    if self.heap_array[2*n - 1][1] < self.heap_array[n - 1][1]:
                        self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
                        n = 2*n
                    else:
                        break
                else:
                    if self.heap_array[2*n][1] < self.heap_array[n - 1][1]:
                        self.heap_array[2*n], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n]
                        n = 2*n + 1
                    else:
                        break
                    
            if 2*n == len(self.heap_array):
                if self.heap_array[2*n - 1][1] < self.heap_array[n - 1][1]:
                    self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
        
        else:
            return_value = None
        return(return_value)
        
    def show_root(self):
        return self.heap_array[0] if self.heap_array != [] else None
    
vertices_and_weights = min_heap([([i], weights[i]) for i in range(len(weights))])
huffman_dict = dict(zip(range(len(weights)), ['' for _ in range(len(weights))]))

while len(vertices_and_weights.heap_array) > 1:
    vertex_0 = vertices_and_weights.extract()
    vertex_1 = vertices_and_weights.extract()
    
    for vertex in vertex_0[0]:
        huffman_dict[vertex] = '0' + huffman_dict[vertex]
        
    for vertex in vertex_1[0]:
        huffman_dict[vertex] = '1' + huffman_dict[vertex]
        
    vertices_and_weights.insert((vertex_0[0] + vertex_1[0], vertex_0[1] + vertex_1[1]))
    
print('Longest encoding length:', max([len(i) for i in huffman_dict.values()]))
print('Shortest encoding length:', min([len(i) for i in huffman_dict.values()]))    
    
    

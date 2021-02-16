#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Compute minimum weight indpendent subset of a path graph

with open('mwis.txt', 'r') as f:
    weights = [int(i) for i in f.read().split('\n')[1:-1]]


# Iteratively build solutions for first i vertices
iteration_weights = [weights[0], max(weights[:2])]
for i in range(2, len(weights)):
    if iteration_weights[i - 1] >  weights[i] + iteration_weights[i - 2]:
        iteration_weights.append(iteration_weights[i - 1])
    else:
        iteration_weights.append(weights[i] + iteration_weights[i - 2])
    
# Reverse engineer path based on weights at each iteration
i = len(iteration_weights) - 1
s = []
while i > 1:
    if iteration_weights[i - 1] > iteration_weights[i - 2] + weights[i]:
        i -= 1
    else:
        s.append(i)
        i -= 2

if i == 0:
    s.append(0)
else:
    s.append(max([0, 1], key = lambda x: weights[x]))

# Print binary string indicating which of a list of vertices (indexed from 1) is included
# in the maximum weight independent set
result = ''  
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
    if i - 1 in s:
        result += '1'
    else:
        result += '0'
        
print(result)
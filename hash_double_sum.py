# -*- coding: utf-8 -*-

with open('algo1-programming_prob-2sum.txt', 'r') as f:
    input_array = [int(x) for x in f.read().split('\n')[:-1]]

# Create list to track numbers t in interval [-10000, 10000] such that there exist distinct x and y in 
# the input array that satisfy x + y = t
distinct_sum = set()
for t in range(-10000, 10001):
    numbers_seen = set()
    for i in input_array:
        if (t - i) in numbers_seen:
            if t - i != i:
                distinct_sum.add(t)
                break
        else:
            numbers_seen.add(i)
            
    
            
            
        
    
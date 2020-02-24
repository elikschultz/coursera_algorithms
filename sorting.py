#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementations of various sorting algorithms.
"""
def selection_sort(x):
    for i in range(len(x)):
        min_val = x[i]
        min_j = i
        # Find minimum value in unsorted portion of list
        for j in range(i, len(x)):
            if x[j] < min_val:
                min_j, min_val = j, x[j]    
        x[i], x[min_j] = x[min_j], x[i]
    return(x)

def insertion_sort(x):
    y = []
    for i in x:
        y += [i]
        # Iteratively add elements of x to sorted list y
        for j in range(len(y)):
            if y[-1] < y[j]:
                y = y[0:j] + [y[-1]] + y[j:-1]
                break
    return(y)
        
def bubble_sort(x):
    loop_tracker = True
    while loop_tracker == True:
        loop_tracker = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                loop_tracker = True
    return(x)
    
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
        if x_1[counter_1] < x_2[counter_2]:
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
    
def quick_sort(x):
    if len(x) <= 1:
        return(x)
    else:
        # Make sure pivot is in correct position
        pivot = x[len(x)//2]
        x[0], x[len(x)//2] = x[len(x)//2], x[0]
        j = 0 # Every entry with index <= j should be <= pivot 
        for i in range(1, len(x)):
            if x[i] < pivot:
                x[j + 1], x[i] = x[i], x[j + 1]
                j += 1
        x[0], x[j] = x[j], x[0]
        
        # Perform recursive calls
        x_1 = quick_sort(x[:j])
        if (j < len(x)):
            x_2 = quick_sort(x[(j + 1):])
        else:
            x_2 = []
        return(x_1 + [x[j]] + x_2)

            
            
        
    
                
        
    

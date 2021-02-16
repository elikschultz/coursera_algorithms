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
    
def quick_sort(x, pivot_method = "middle"):
    if len(x) <= 1:
        return(x, 0)
        
    else:
        if pivot_method == "middle":
            pivot = x[len(x)//2]
            pivot_loc = len(x)//2
            
        elif pivot_method == "first":
            pivot = x[0]
            pivot_loc = 0
            
        elif pivot_method == "last":
            pivot = x[-1]
            pivot_loc = len(x) - 1
            
        elif pivot_method == "median_three":
            if len(x) % 2 == 0:
                median_three = {x[0]: 0,
                                x[-1]: len(x) - 1,
                                x[int(len(x)/2) - 1]: len(x)/2 - 1}
                pivot = insertion_sort([x[0], x[-1], x[int(len(x)/2) - 1]])[1]
                pivot_loc = int(median_three[pivot])
            else:
                median_three = {x[0]: 0,
                                x[-1]: len(x) - 1,
                                x[int((len(x) - 1)/2)]: (len(x) - 1)/2}
                pivot = insertion_sort([x[0], x[-1], x[int((len(x) - 1)/2)]])[1]
                pivot_loc = int(median_three[pivot])
    
        x[0], x[pivot_loc] = x[pivot_loc], x[0]
        i = 1
        for j in range(1, len(x)):
            if x[j] < pivot:
                x[i], x[j] = (x[j], x[i]) 
                i += 1
                
        x[i - 1], x[0] = x[0], x[i - 1]
        # Perform recursive calls
        x_1, c_1 = quick_sort(x[:(i - 1)], pivot_method)
        if (j < len(x)):
            x_2, c_2 = quick_sort(x[i:], pivot_method)
        else:
            x_2, c_2 = ([], 0)
        return(x_1 + [x[i-1]] + x_2, c_1 + len(x) - 1 + c_2)
        
with open('QuickSort.txt', 'r') as f:
    test_array = [int(x) for x in f.read().split('\n')[:-1]]

print(quick_sort(test_array.copy(), 'first')[1])
print(quick_sort(test_array.copy(), 'last')[1])
print(quick_sort(test_array.copy(), 'median_three')[1])


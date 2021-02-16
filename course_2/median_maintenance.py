# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:11:47 2020

@author: eschultz
"""
class heap():
    def __init__(self, heap_type = 'min', array = []):
        self.heap_array = []
        self.heap_type = heap_type
        for item in array:
            self.insert(item)
        
    def insert(self, key):
        self.heap_array.append(key)
        n = len(self.heap_array)
        
        if self.heap_type == 'min':
            while n > 1:
                if self.heap_array[n//2 - 1] > self.heap_array[n - 1]:
                    self.heap_array[n//2 - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[n//2 -1]
                    n = n//2
                else:
                    break
                
        elif self.heap_type == 'max':
            while n > 1:
                if self.heap_array[n//2 - 1] < self.heap_array[n - 1]:
                    self.heap_array[n//2 - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[n//2 -1]
                    n = n//2
                else:
                    break
            
    def extract(self):
        if self.heap_array != []:
            self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0]
            return_value = self.heap_array.pop()
            n = 1
            
            if self.heap_type == 'min':
                while 2*n + 1 <= len(self.heap_array):
                    if self.heap_array[2*n - 1] < self.heap_array[2*n]:
                        if self.heap_array[2*n - 1] < self.heap_array[n - 1]:
                            self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
                            n = 2*n
                        else:
                            break
                    else:
                        if self.heap_array[2*n] < self.heap_array[n - 1]:
                            self.heap_array[2*n], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n]
                            n = 2*n + 1
                        else:
                            break
                        
                if 2*n == len(self.heap_array):
                    if self.heap_array[2*n - 1] < self.heap_array[n - 1]:
                        self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
                        
            elif self.heap_type == 'max':
                while 2*n + 1 <= len(self.heap_array):
                    if self.heap_array[2*n - 1] > self.heap_array[2*n]:
                        if self.heap_array[2*n - 1] > self.heap_array[n - 1]:
                            self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
                            n = 2*n
                        else:
                            break
                    else:
                        if self.heap_array[2*n] > self.heap_array[n - 1]:
                            self.heap_array[2*n], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n]
                            n = 2*n + 1
                        else:
                            break
                        
                if 2*n == len(self.heap_array):
                    if self.heap_array[2*n - 1] > self.heap_array[n - 1]:
                        self.heap_array[2*n - 1], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[2*n - 1]
        else:
            return_value = None
        return(return_value)
        
    def show_root(self):
        return self.heap_array[0] if self.heap_array != [] else None
    
medians = []   
with open('Median.txt', 'r') as f:
    values = list(map(int, f.read().split('\n')[:-1]))
    
max_heap = heap(heap_type = 'max')
min_heap = heap(heap_type = 'min')

for i in values:
    if len(max_heap.heap_array) == len(min_heap.heap_array):
        if max_heap.heap_array == []:
            max_heap.insert(i)
        elif i <= max_heap.show_root():
            max_heap.insert(i)
        else:
            min_heap.insert(i)
            max_heap.insert(min_heap.extract())
            
    else:
        if min_heap.heap_array == []:
            if i < max_heap.show_root():
                max_heap.insert(i)
                min_heap.insert(max_heap.extract())
            else:
                min_heap.insert(i)
        elif i <= max_heap.show_root():
            max_heap.insert(i)
            min_heap.insert(max_heap.extract())
        else:
            min_heap.insert(i)
            
    medians.append(max_heap.show_root())
            
print(sum(medians) % 10000)     
    
        
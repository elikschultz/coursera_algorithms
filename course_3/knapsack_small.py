# -*- coding: utf-8 -*-

with open('knapsack1.txt', 'r') as f:
    knapsack_capacity = int(f.readline().split()[0])
    items = [(int(i.split()[0]), int(i.split()[1])) for i in f.read().split('\n')[:-1]]

# Create an array where i, j entry corresponds to opitmal size of subproblem over first 
# i items with knapsack capacity j
solutions = []
for i in range(len(items)):
    solutions_i = []
    for j in range(knapsack_capacity + 1):
        if i == 0: 
            if items[i][1] > j:
                solutions_i.append(0)
            else:
                solutions_i.append(items[i][0])
        else:
            if items[i][1] > j:
                solutions_i.append(solutions[i - 1][j])
            elif items[i][0] + solutions[i - 1][j - items[i][1]] > solutions[i - 1][j]:
                solutions_i.append(items[i][0] + solutions[i - 1][j - items[i][1]])
            else:
                solutions_i.append(solutions[i - 1][j])

    solutions.append(solutions_i)
            
print('Optimal solution value for small problem: ', solutions[len(items) - 1][knapsack_capacity])        
        
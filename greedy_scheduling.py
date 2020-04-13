# -*- coding: utf-8 -*-

with open('jobs.txt', 'r') as f:
    jobs = [(int(i.split()[0]), int(i.split()[1])) for i in f.read().split('\n')[1:-1]]

def merge_sort_tuples(x):
    if len(x) == 1:
        return x
    x_1 = merge_sort_tuples(x[:int(len(x)/2)])
    x_2 = merge_sort_tuples(x[int(len(x)/2):])
    
    return(merge_tuples(x_1, x_2))
    
def merge_tuples(x_1, x_2):
    result = []        
    counter_1 = 0
    counter_2 = 0
       
    # Iterate through sorted sublists in parallel, create combined sorted list                
    while counter_1 < len(x_1) and counter_2 < len(x_2):
        if x_1[counter_1][0] < x_2[counter_2][0]:
            result += [x_1[counter_1]]
            counter_1 += 1
            
        elif x_1[counter_1][0] > x_2[counter_2][0]:
            result += [x_2[counter_2]]
            counter_2 += 1
            
        else:
            if x_1[counter_1][1] < x_2[counter_2][1]:
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

# Compute sum of weighted completion times, executing in order of decreasing difference between weight and length
job_diffs = merge_sort_tuples([(job[0] - job[1], job[0]) for job in jobs])
job_diffs.reverse()

time_elapsed = 0
total_cost = 0
for job in job_diffs:
    time_elapsed += job[1] - job[0]
    total_cost += time_elapsed * job[1]
    
print('Total cost using weight - length:', total_cost)
    
# Compute sum of weighted completion times, executing in order of decreasing weight/length ratio
job_ratios = merge_sort_tuples([(job[0]/job[1], job[0]) for job in jobs])
job_ratios.reverse()

time_elapsed = 0
total_cost = 0
for job in job_ratios:
    time_elapsed += job[1]/job[0]
    total_cost += time_elapsed * job[1]
print('Total cost using weight/length:', total_cost)


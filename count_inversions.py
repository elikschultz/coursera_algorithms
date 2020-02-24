"""
Inversion Counting
"""
# Returns sorted copy of array and inversion count
def count_and_sort(arg):
    n = len(arg)
    if n == 1:
        return(arg, 0)
        
    left_sort, left_count = count_and_sort(arg[:int(len(arg)/2)])
    right_sort, right_count = count_and_sort(arg[int(len(arg)/2):])
    
    inversion_count = 0
    result = []        
    counter_1 = 0
    counter_2 = 0
    
    # Iterate through sorted sublists in parallel, create combined sorted list
    # and count inversions                   
    while counter_1 < len(left_sort) and counter_2 < len(right_sort):
        if left_sort[counter_1] < right_sort[counter_2]:
            result += [left_sort[counter_1]]
            counter_1 += 1
        else:
            result += [right_sort[counter_2]]
            counter_2 += 1
            inversion_count += len(left_sort) - counter_1
            
    if counter_1 == len(left_sort):
        if type(right_sort[counter_2:]) == list:
            result += right_sort[counter_2:]
        else:
            result += [right_sort[counter_2]]
            
    else:
        if type(left_sort[counter_1:]) == list:
            result += left_sort[counter_1:]
        else:
            result += [left_sort[counter_1]]
            
    return(result, inversion_count + left_count + right_count)
 
# Get input file to test function
with open('IntegerArray.txt') as f:
    input_array = f.read()

# Convert input to list and run function    
input_array = [int(i) for i in input_array.split('\n')[:-1]]

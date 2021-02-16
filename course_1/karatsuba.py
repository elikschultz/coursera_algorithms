"""
Implementation of Karatsuba multipliation.
"""

# Define sign function for use in main Karatsuba function
def sign(n):
    if (n > 0):
        return 1
    if (n < 0):
        return -1
    if (n == 0):
        return 0

# Recursive function that performs Karatsuba multiplication
def karatsuba(int_1, int_2):
    int_1 = str(int_1)
    int_2 = str(int_2)
    n = len(int_1)
    
    if (n == 1):
        return(int(int_1) * int(int_2))

    # Split each input in half
    a = int_1[:int(n/2)]
    b = int_1[int(n/2):]
    c = int_2[:int(n/2)]
    d = int_2[int(n/2):]
    
    # Perform recursive calls and combine results
    result_1 = karatsuba(a, c)
    result_2 = karatsuba(b, d)
    
    # Compute ad + bc
    arg_1 = int(a) - int(b)
    arg_2 = int(d) - int(c)
    sign_adj = sign(arg_1) * sign(arg_2)
    arg_1 = str(abs(arg_1))
    arg_2 = str(abs(arg_2))
    
    if len(arg_1) < n/2:
        arg_1 = '0'* int(n/2 - len(arg_1)) + arg_1
    if len(arg_2) < n/2:
        arg_2 = '0' * int(n/2 - len(arg_2)) + arg_2
        
    result_3 = sign_adj*karatsuba(arg_1, arg_2) + result_1 + result_2
    
    # Combine results
    result = 10**n * result_1 + 10**(int(n/2)) * result_3  + result_2
    return(result)

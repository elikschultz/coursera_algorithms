# -*- coding: utf-8 -*-

class knapsack():
    def __init__(self, file_name = None):
        if file_name == None:
            self.capacity = None
            self.items = None
        else:
            try:
                with open(file_name, 'r') as f:
                    self.capacity = int(f.readline().split()[0])
                    self.items = [(int(i.split()[0]), int(i.split()[1])) for i in f.read().split('\n')[:-1]]
            except:
                print('Invalid filename provided.')
        
        self.subproblem_solutions = {}
        
    # Define method to recursively copmute subproblem solutions to avoid solving unneeded subproblems 
    # (as may happen in iterative approach)    
    def optimal_subset_solution(self, n_items, target_capacity):
        '''n_items: include items up to n_items-ith item, target_capacity: capacity of knapsack in subproblem'''
        if (n_items, target_capacity) in self.subproblem_solutions.keys():
            return self.subproblem_solutions[(n_items, target_capacity)]
        else:
            if n_items == 0:
                if self.items[0][1] <= target_capacity:
                    self.subproblem_solutions[(n_items, target_capacity)] = self.items[0][0]
                    return self.items[0][0]
                else:
                    self.subproblem_solutions[(n_items, target_capacity)] = 0
                    return 0
            else:
                option_0 = self.optimal_subset_solution(n_items - 1, target_capacity)
                if target_capacity - self.items[n_items][1] <= 0:
                    if n_items == len(self.items) - 1 and target_capacity == self.capacity:
                        self.subproblem_solutions = {}
                        return option_0
                    self.subproblem_solutions[(n_items, target_capacity)] = option_0
                    return option_0
                else: 
                    option_1 = self.optimal_subset_solution(n_items - 1, target_capacity - self.items[n_items][1]) + self.items[n_items][0]
                    if n_items == len(self.items) - 1 and target_capacity == self.capacity:
                        self.subproblem_solutions = {}
                        return max([option_0, option_1])
                    self.subproblem_solutions[(n_items, target_capacity)] = max([option_0, option_1])
                    return max([option_0, option_1])
                
    def print_optimal_solution(self):
        print('Optimal solution: ', self.optimal_subset_solution(len(self.items) - 1, self.capacity))
          
knapsack_big = knapsack('knapsack_big.txt')
knapsack_big.print_optimal_solution()

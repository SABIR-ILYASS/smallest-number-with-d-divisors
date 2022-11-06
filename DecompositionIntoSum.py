# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:30:26 2022

@author: sabir
"""

class DecompositionIntoSum:
    def __init__(self, n, m):
        self.integer = n
        self.max_length = m
        self.list_first_zero = []
    
    def sous_decomposition(self, L, sum_L, first):
        res = []
        res.append(L)
        L_step = L[:]
        while(L_step[1] != sum_L - L_step[0]):
            L_step[1] = L_step[1] + L_step[2]
            self.list_first_zero.append(first)
            first -= 1
            L_step[first] = 0
            res.append(L_step[:])
        self.list_first_zero.append(first)
        return res
    
    def change_first_element(self, L, first_zero):
        L[0] = L[0] + 1
        L[first_zero - 1] = 0
        return L
    
    def decomposition_of_number(self):
        n = self.integer
        L = [1 for i in range(n)]
        L[0] = n + 1 - self.max_length
        for m in range(n - self.max_length):
            L[self.max_length + m] = 0
        
        result = []
        first_zero = self.max_length
            
        for i in range(self.max_length):
            ss_decomp = self.sous_decomposition(L[:], n, first_zero)
            result.extend(ss_decomp[:])
            self.change_first_element(L, first_zero)
            first_zero -= 1
        return result

deco = DecompositionIntoSum(3, 3)
print(deco.decomposition_of_number())
print(deco.list_first_zero)
# -*- coding: utf-8 -*-
"""
@author: sabir, 2022.
"""
import DecompositionIntoSum as DS

class DecompositionIntoProduct:
    def __init__(self, n):
        self.integer = n
        
    def firstDivisor(self, n):
        if (n == 0 or n == 1):
            return 1
        for i in range(2,n+1):
            if n%i == 0:
                break
        return i
    
    def listOfDivisor(self):
        l=[1]
        m= self.integer
        while m != 1:
            l.append(self.firstDivisor(m))
            m = m // self.firstDivisor(m)
        return l[1:]

    #the function removes repeated numbers in a given list
    def noRepeat(self, l):
        M=[l[0]]
        for i in range(1,len(l)):
            if not (l[i] in l[:i]):
                M.append(l[i])
        return M
    
    # The following function returns the p-adic valuation of an integer, where p is a prime number
    def counter(self):
        l = self.listOfDivisor()
        M = self.noRepeat(l)
        K = []
        for i in M:
            K.append(l.count(i))
        return K

    # This increment function proposes an increment method to browse a list, it will help us to
    # determine the divisors of an integer
    def incr(self, l,K):
        i=0
        while l[i] == K[i]:
            if i < len(l)-1:
                i = i+1
            else:
                break
        l[i] = l[i]+1
        for j in range(i):
            l[j]=0
        return l

    # The following function will help us calculate the number of divisors of an integer
    def prod(self, l):
        p=1
        for i in range(len(l)):
            p=p*(1+l[i])
        return p
    
    # The main function: gives the list of positive divisors of an integer given as input
    def division(self):
        l = self.listOfDivisor()
        M = self.noRepeat(l)
        K = self.counter()
        D = [1]
        L = [0 for i in range(len(K))]
        for i in range(self.prod(K)-1):
            d = 1
            Y = self.incr(L,K)
            for i in range(len(M)):
                d = d*(M[i]**Y[i])
            D.append(d)
        return sorted(D)
    
    def change_first_element(self, L, n):
        for i in range(n - 1):
            L[i]= L[i + 1]       
        L[n - 1] = L[0]
        return L
    
    def sous_decomposition(self, L, prod_L, size):
        res = []
        L_step = L[:]
        while(L_step[1] != prod_L // L_step[0]):
            L_step[1] = L_step[1] * L_step[2]
            for i in range(2, size - 1):
                L[i] = L[i + 1]
            res.append(L_step[:])
            size -= 1
        return res
    """
    def decomposition_of_number_into_product(self):
        n = self.integer
        L = self.listOfDivisor() 
        result = []
        result.append(L)
        size = len(L)
        first_zero = size           
        for i in range(size):
            ss_decomp = self.sous_decomposition(L[:first_zero], n, first_zero)
            result.extend(ss_decomp[:first_zero])
            self.change_first_element(L, first_zero)
            first_zero -= 1
        return result
    """

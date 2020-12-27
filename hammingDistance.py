# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:41:46 2020

@author: kalan
"""

#461. Hamming Distance
# =============================================================================
# 
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 2^31.
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#        
# =============================================================================
# =============================================================================
# To convert integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient and the remainder. Continue dividing the quotient by 2 until you get a quotient of zero. Then just write out the remainders in the reverse order.
# 
# Here is an example of such conversion using the integer 12.
# First, let’s divide the number by two specifying quotient and remainder:
# 
# =============================================================================





##standardize two inputs to same size --- with leading zeros if needed --max is 32

class Solution:
    def hammingDistance(self, x,y):
        import math as m

        def convtodec(num):
            
            
            div= num
            if div == 0:
                quit
            else:
                div = m.floor(num/2)
                mod = (num % 2)
 #               print(div,mod)
                out.append(mod)
                convtodec(div)


        out=[]
        convtodec(x)
        out.reverse()
        a= out
        out=[]
        convtodec(y)
        out.reverse()
        b= out 
        
        while len(a) > len(b):
            #b needs to be normalized
            b.insert(0,0)
        
        while len(b) > len(a):
            a.insert(0,0)
        
        zip_obj = zip(a,b)
        difference = []
        for i,j in zip_obj:
            difference.append(abs(i-j))
        
#        print(difference)
        diff = sum(difference)
        return diff
    
a=Solution()
a.hammingDistance(1, 4)



       
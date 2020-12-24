# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:38:50 2020

@author: kalan
"""

# =============================================================================
# 905. Sort Array By Parity
# Easy
# 
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# Example 1:
#  
# num =[3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# =============================================================================


num =[3,1,2,4]


class Solution:
    def sortArrayByParity(self, A):
        out_even=[]
        out_odd=[]
        for i in num:
            if i%2 == 0:
                out_even.append(i)
            else:
                out_odd.append(i)
        
        
        out = out_even + out_odd
        return out
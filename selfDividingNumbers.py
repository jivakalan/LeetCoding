# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:40:10 2020

@author: kalan
"""
# =============================================================================
# 
# A self-dividing number is a number that is divisible by every digit it contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
# 
# =============================================================================
# =============================================================================
# Example 1:
# =============================================================================
Input: 
left = 1 
right = 22
Output: [66,708]


class Solution:
    def selfDividingNumbers(self, left,right):
        
        out=[]
        for number in range(left,right+1):

                cnt=0                    
                for digit in str(number):
                    if int(digit)==0:
                        break
                    if number % int(digit) == 0:
                        cnt+=1
                        #print(number,cnt)
                    
                    if cnt == len(str(number)):
                          
                        out.append(number)
        return out 
    
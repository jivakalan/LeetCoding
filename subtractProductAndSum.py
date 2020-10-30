# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:56:58 2020

@author: kalan
"""
# =============================================================================
# 
# 1281. Subtract the Product and Sum of Digits of an Integer
# =============================================================================
# # =============================================================================
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#  
# 
# Example 1:
# 
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# =============================================================================

  

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        num_as_list = [int(i) for i in str(n)]
        
        sum_of_digits=0
        product_of_digits = 1
        for digit in num_as_list:
            sum_of_digits=sum_of_digits+digit
            product_of_digits = product_of_digits * digit
        
        return product_of_digits-sum_of_digits        

a=Solution()
a.subtractProductAndSum(n=4421)  
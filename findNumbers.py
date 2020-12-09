# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:43:24 2020

@author: kalan
"""
# =============================================================================
# 
# 1295. Find Numbers with Even Number of Digit
# Given an array nums of integers, return how many of them contain an even number of digits.
#  
# 
# Example 1:
# 
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
# 
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
# =============================================================================

nums = [12,345,2,6,7896]

nums = [555,901,482,1771]



class Solution:
    def findNumbers(self, nums):
        
        cnt=0
        for i in nums:
            if len(str(i))%2 ==0:
                cnt+=1     
        return cnt
    
a=Solution()
a.findNumbers(nums)        
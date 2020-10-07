# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:39:03 2020

@author: jkalan
"""

# =============================================================================
# 
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the 
#  array, and it should return false if every element is distinct.
# 
# Input: [1,2,3,1]
# Output: true
# =============================================================================
# 
# Example 3:
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# =============================================================================
# =============================================================================

nums = [1,2,3,3]

class Solution(object):
    
    def containsDuplicate(self, nums):
    
        for i in nums:
            if nums.count(i)>1:
                return True
        return False

a=Solution()
a.containsDuplicate(nums)


#time limit exceeded
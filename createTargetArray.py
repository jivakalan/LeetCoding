# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:50:02 2020

@author: jkalan
"""

# =============================================================================
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# 
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# 
# It is guaranteed that the insertion operations will be valid.
# 
#  
# 
# Example 1:
# 
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
# Example 2:
# 
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
# Example 3:
# 
# Input: nums = [1], index = [0]
# Output: [1]
# =============================================================================



class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target=[]
        for i in range(0,len(nums)):
            print(nums[i], index[i])
            target.insert(index[i],nums[i])

        return target
        
a=Solution()
targ= a.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])
# Input: 
# Output: [0,4,1,3,2]

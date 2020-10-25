# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:38:24 2020

@author: kalan
"""
# =============================================================================
# 
# 1207. Unique Number of Occurrences

# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Example 1:
# 
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
# 
# Input: arr = [1,2]
# Output: false
# Example 3:
# 
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#  
# 
# Constraints:
# 
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
# =============================================================================

arr = [1,2,2,1,1,3]
       

    
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
            #scan dictionary to see if there are unique occurences
        if len(set(dic.values())) == len(set(dic.keys())):
            return True    
        else:
            return False
a=Solution()
a.uniqueOccurrences( [-3,0,1,-3,1,1,1,-3,10,0])
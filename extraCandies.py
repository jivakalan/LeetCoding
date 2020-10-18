# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:16:57 2020

@author: jkalan
# =============================================================================
# """
# Example 1:
# 
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# 
# Example 2:
# 
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# 
# Example 3:
# 
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
# =============================================================================
 
##first approach - Brute Force
##get the max of the array and compare each element to it

candies = [2,3,5,1,3]
extraCandies = 3

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        out=[]
        for i in candies:
            out.append(i+extraCandies >= max(candies))
        return out
    
a=Solution()
out=a.kidsWithCandies(
                    candies = [12,1,12]
                    ,extraCandies = 10)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:27:43 2020

@author: jkalan
"""
# =============================================================================
# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# 
# A subarray is a contiguous subsequence of the array.
# 
# Return the sum of all odd-length subarrays of arr.
# 
#  
# 
# Example 1:
# 
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sum
# arr = [1,4,2,5,3]
# =============================================================================

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def sum_subarray(sublength):
            
            c=0
            for i in range(0,len(arr)):
                s=i            
                e = s+ sublength
                subarray = arr[s:e]
                
                
                if len(subarray) == sublength:
                    print(subarray)
                    c= c+sum(subarray)
            return c
                    
        
        tot=0
        for i in range(0,len(arr)+1):
            #0,3,5
            if i%2!=0:
                tot=tot+sum_subarray(i)
            
        return tot   

a=Solution()
a.sumOddLengthSubarrays(arr = [1,4,2,5,3])
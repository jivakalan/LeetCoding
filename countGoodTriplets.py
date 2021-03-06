# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:36:34 2020

@author: kalan
"""

# =============================================================================
# 1534. Count Good Triplets
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# 
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# 
# Return the number of good triplets.
# 
#  
# 
# Example 1:
# 
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# Example 2:
# 
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.
#  
# =============================================================================

12:05
12:10
(index error )
12:11 (incorrect count)

arr = [3,0,1,1,9,7]
a = 7 
b = 2 
c = 3


class Solution:
    def countGoodTriplets(self,arr,a,b,c):
        
           
        cnt=0
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                for k in range(0, len(arr)) :
                    if i<j<k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                      #  print(arr[i],arr[j],arr[k])
                        cnt+=1
                    
        return cnt
    
s=Solution()
s.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)
        
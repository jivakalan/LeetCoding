<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:38:19 2020

@author: jkalan
"""

# =============================================================================
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
=======

# =============================================================================
# 
# n a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
>>>>>>> b37e0598de8bda76b3da25d0b55bd9986a34e06c
# 
# Return the element repeated N times.
# 
#  
# 
# Example 1:
# 
# Input: [1,2,3,3]
# Output: 3
# Example 2:
# 
# Input: [2,1,2,5,3,2]
# Output: 2
# Example 3:
# 
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
#  
# 
# Note:
# 
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even
# =============================================================================
<<<<<<< HEAD
=======

nums =  [1,2,3,3]

     
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        dic={}

        for i in range(0, len(A)):
            if A[i] in dic:
                print(dic)
                dic[A[i]]+=1
                print(dic)
            else:
                dic[A[i]] = 1 
        maxval= max(dic, key= dic.get)
        return maxval

a=Solution()
a.repeatedNTimes(nums)                

>>>>>>> b37e0598de8bda76b3da25d0b55bd9986a34e06c

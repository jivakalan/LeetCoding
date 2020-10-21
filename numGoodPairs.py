# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:43:36 2020

@author: jkalan
"""
# =============================================================================
# 
# 1512. Number of Good Pairs
# Share
# Given an array of integers nums.
# 
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# 
# Return the number of good pairs.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
# 
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# =============================================================================

nums = [1,2,3,1,1,3]
##out = 4
##brute force is 0(N^2)

#how to speed it up ---divide by 2...hashmap? 
#sort...1,1,1,2,3,3--stll n squared
#hashmap
        

class Solution(object):
    def numgoodPairs(self,nums):
        
        c=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                
                if nums[i]==nums[j] and i < j:
                    #print(i,j)
                    c+=1 
        return c
                
               
a=Solution()                

a.numgoodPairs(nums = [1,1,1,1])

# ==========================================================================


nums = [1,2,3,1,1,3]
##out = 4


#how to speed it up ---divide by 2...hashmap? 
#sort...1,1,1,2,3,3--stll n squared
#hashmap is the right approach 


#class Solution2(object):
 #   def numgoodPairs2(self,nums):
        mydict={}
        c=0
        for i in range(0,len(nums)):
            mydict[i] =nums[i] 
            if nums[i] in mydict:
                c+=1
                
  #      return c
                
  
a=Solution()                     
b=Solution2()      

a.numgoodPairs(nums =  [1,2,3,1,1,3])          
b.numgoodPairs2(nums =  [1,2,3,1,1,3])        

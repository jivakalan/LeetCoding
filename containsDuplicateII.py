# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:22:39 2020

@author: jkalan
"""

# =============================================================================
# Given an array of integers and an integer k, find out whether there are two 
# distinct indices i and j in the array such that nums[i] = nums[j] and the absolute 
# difference between i and j is at most k.

# Example 1:
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true


# Example 2:
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# =============================================================================

#worst case - they are at opposite ends (if i start from the beginning)
#ori n the middle if i start from opposite ends


#complexity analysis ...o(n2)

#brute force then optimize


nums =  [1,2,3,1]
k = 3

class Solution_1(object):
    def containsNearbyDuplicate2(self,nums,k):
                
                for i in range(0,len(nums)):
                    for j in range(0,len(nums)):
                        #print(i,j,nums[i]==nums[j],i!=j,abs(i-j))
                        if nums[i]==nums[j] and i!=j and abs(i-j)<=k:
                            return True
                       
                return False
a=Solution_1()                

a.containsNearbyDuplicate2(nums = [1,0,1,1], k = 1)

##testing commmit 

######################time limit exceeded on above solution

#try creating hash table 

# =============================================================================
# Given an array of integers and an integer k, find out whether there are two 
# distinct indices i and j in the array such that nums[i] = nums[j] and the absolute 
# difference between i and j is at most k.

# Example 1:
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# =============================================================================


class Solution(object):
    def containsNearbyDuplicate(self,nums,k):        
                
        mydict={}           
        for i in range(0,len(nums)):
            if nums[i] in mydict and i-mydict[nums[i]]<=k:
                return True
                break
            else:
                mydict[nums[i]]= i
        return False
    
a=Solution()                

a.containsNearbyDuplicate( [1,2,3,1,2,3], k = 2)

nums=[1,0,1,1]
k = 1
    
mydict={}           
for i in range(0,len(nums)):
    if nums[i] in mydict and i-mydict[nums[i]] <= k:
        print('True')
    else:
        mydict[nums[i]]= i
   


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
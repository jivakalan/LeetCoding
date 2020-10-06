# -*- coding: utf-8 -*-
# =============================================================================
# 
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# 
# Return the running sum of nums.
# =============================================================================

# =============================================================================
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
#
# =============================================================================

nums = [1,1,1,1,1]

class Solution(object):
    def runningSum(self,nums):
        out = nums  
        for i in range(0,len(nums)):
            if i ==0:
                out[i]= nums[i]
            else:
                out[i]=out[i-1]+nums[i] 
        return out 
     
        
            
a= Solution()
a.runningSum(nums)
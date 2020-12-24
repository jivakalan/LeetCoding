# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:52:37 2020

@author: kalan
"""
# =============================================================================
# 
# 1304. Find N Unique Integers Sum up to Zero
# 
# Given an integer n, return any array containing n unique integers such that they add up to 0.
# 
#  
# 
# Example 1:
# 
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
# 
#     
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
# 
# Input: n = 1
# Output: [0]
# =============================================================================

import random

class Solution:
    def sumZero(self, n):
        
        out=[]
        if n%2 ==0:
            #a=int(n/2)
            
            while len(out) < n:
                num = random.randint(1,1000)
                if num in out:
                    continue
                else:
                    
                    out.append(num)
                    out.append(-num) 
        else:
           # a=int((n-1)/2)
            while len(out) < n-1:
                num = random.randint(1,1000)
                if num in out:
                    continue
                else:
                    
                    out.append(num)
                    out.append(-num) 
            out.append(0)
            
        return out
    


a=Solution()
out= a.sumZero(n=5)



#accepted in 15
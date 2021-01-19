# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:12:47 2021

@author: kalan
"""

# =============================================================================
# 9. Palindrome Number
# 
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# 
# =============================================================================
 

x =121

class Solution:
    def isPalindrome(self, x):
              
        out =[]
        for i in range(len(str(x)),0,-1 ):
         
            out.append(str(x)[i-1])
        
        if list(str(x)) == out :
            return True
        else:
            return False

a=Solution()

a.isPalindrome(x)
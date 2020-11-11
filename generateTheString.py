# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:18:29 2020

@author: jkalan
"""
# =============================================================================
# 1374. Generate a String With Characters That Have Odd Counts
# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
# 
# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
# 
# Example 1:
# 
# Input: n = 4
# Output: "pppz"
# 
# =============================================================================
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2 == 0:

            remainder = n - 1

            newstring = remainder*'a'

            newstring = newstring +'b'
        else: 
            newstring = n * 'a'
        return newstring
    
    
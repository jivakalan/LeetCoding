# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:18:29 2020

@author: jkalan
"""
# =============================================================================
# 1374. Generate a String With Characters That Have Odd Counts
# Given an integer n, return a string with n characters such that each character in such
#  string occurs an odd number of times.
# 
# The returned string must contain only lowercase English letters. If there are multiples valid 
# strings, return any of them.  
# 
# Example 1:
# 
# Input: n = 4
# Output: "pppz"
# 
# =============================================================================

if n is odd : n=1,3,5,7,etc
if n is even n=2,4,6,8
if n = 0 :
    
n =1
any single letter ...eg: a
n=3  3 singles - a b c 
n=5  5 singles -- a b d d e 
     2 singles and triplet --- a b ccc
n-7  7 singles  a b  c d e f g
     4 singles and a triplet a b c d eee
     2 singles and a pentuplet  a b ccccc
     
n=2  2 singles
n=4  triplet + single ccc a
     4 singles
n=6 ; 6 singles     

     
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        
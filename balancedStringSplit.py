# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:38:01 2020

@author: kalan
"""

# =============================================================================
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# 
# Given a balanced string s split it in the maximum amount of balanced strings.
# 
# Return the maximum amount of splitted balanced strings.
# 
#  
# 
# Example 1:
# 
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
# 
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# =============================================================================


s = "RLRRLLRLRL"

what is the maximum number of BALANCED Strings that can be Created


RL RL RL  RRLL   RLRRLLRLRL  

Output =4


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
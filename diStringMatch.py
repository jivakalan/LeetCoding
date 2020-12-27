# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:26:58 2020

@author: kalan
"""

# =============================================================================
# 942. DI String Match
# easy
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# 
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# 
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#  
# 
# Example 1:
# 
# Input: "IDID"
# Output: [0,4,1,3,2]
# =============================================================================

s= "IDID"

out=[]
for i in range(0,len(s)+1):
    out.append(i)

class Solution:
    def diStringMatch(self, S):
        
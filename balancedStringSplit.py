# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:38:01 2020

@author: kalan
"""

# =============================================================================
# 1221.Balanced strings are those who have equal quantity of 'L' and 'R' characters.
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

s="RLRRRLLRLL"





cnt=0
for i in range(0,len(s),2):
    j=i+2
    print(i,j)
    substring = s[i:j]

    if substring.count('R') == substring.count('L'):
        cnt+=1
   
    
    else:
        j=j+2
        print('else',i,j)
        substring=s[i:j]
        if substring.count('R') == substring.count('L'):
            cnt+=1
            print(substring)
        
        
     






class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cnt =0
        rs=0
        ls=0
        for i in range(0,len(s)):
            if s[i]=='R':
                rs+=1
            if s[i]=='L':
                ls+=1
            if rs == ls:
                cnt+=1
# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 21 22:02:57 2020
# 
# @author: jkalan
# """
# ##1528
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# 
# Example 1:
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
#  
#
# Example 2
# Input: s = "art", indices = [1,0,2]
# Output: "rat"
#  
# 
# Constraints:
#
# s.length == indices.length == n
# 1 <= n <= 100
# s contains only lower-case English letters.
# 0 <= indices[i] < n
# All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).
# =============================================================================


s = "codeleet"

class Solution(object):
    
    def shuffleString(self,s, indices):
        sl=list(s)
        new_string = [0]*len(indices)
        for i in range(0,len(sl)):
            new_string[indices[i]]= sl[i]
        new_sl = ''.join(new_string)
        return new_sl
    
a=Solution()
a.shuffleString(s = "art", indices = [1,0,2])
a.shuffleString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5])



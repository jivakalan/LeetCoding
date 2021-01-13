# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:11:13 2021

@author: kalan
"""
# =============================================================================
# 1684. Count the Number of Consistent Strings
# 
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# 
# Return the number of consistent strings in the array words.
# 
#  
# 
# Example 1:
# 
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
# Example 2:
# 
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
# Example 3:
# 
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
# 
# =============================================================================



allowed ="ab"
words = ["ad","bd","aaab","baa","badab"]

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

  
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]


class Solution:
    def countConsistentStrings(self, allowed, words):
        
        out=0
        for word in words:  
            cnt = 0
            for letter in word:
#                print(letter, word)
                if letter in list(allowed):
                    cnt+=1
            if len(word)==cnt:
                out+=1
        return out
        
        
a=Solution()
a.countConsistentStrings(allowed, words)

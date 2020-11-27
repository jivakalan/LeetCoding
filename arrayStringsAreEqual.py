# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:09:23 2020

@author: kalan
"""
# =============================================================================
# 
# 1662. Check If Two String Arrays are Equivalent
# Easy
# 
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# 
# A string is represented by an array if the array elements concatenated in order forms the string.
# 
#  
# 
# Example 1:
# 
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
# Example 2:
# 
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
# Example 3:
# 
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
# =============================================================================

word1 = ["ab", "c"]
word2 = ["a", "bc"]




class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        str1 =''
        for word in word1:
            for letter in word:
                str1 = str1+letter
        
        str2 =''
        for words in word2:
            for letters in words:
                str2 = str2+letters
        
        if str1 == str2 :
            return True
        else:
            return False
a=Solution()
a.arrayStringsAreEqual(word1, word2)        
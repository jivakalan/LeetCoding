# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:15:03 2020

@author: kalan
"""

# =============================================================================
# 1160. Find Words That Can Be Formed by Characters
# Easy
# You are given an array of strings words and a string chars.
# 
# A string is good if it can be formed by characters from chars (each character can only be used once).
# 
# Return the sum of lengths of all good strings in words.
# 
#  
# 
# Example 1:
# 
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
# 
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
# =============================================================================

words = ["cat","bt","hat","tree"]

chars = "atach"


#can the words in words be formed using characters from char? 


## have to deal with collisions!!!!!!!!

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
                        
        possible = []
        sum=0
        for word in words:
        
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    break
            else:
                possible.append(word)   
                sum+=len(word)

        return outsum

    
a=Solution()
a.countCharacters(words, chars)
a.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")

 



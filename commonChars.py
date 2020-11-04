# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:54:54 2020

@author: kalan
"""

# =============================================================================
#1002. Find Common Characters
# =============================================================================
# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
# 
# =============================================================================
# Example 1:
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# =============================================================================


    
class Solution(object):
    def commonChars(self, words):
        
        #fix this - its hard coded!
        unique=set(words[0])
        for i in range(0,len(words)):
            unique= unique.intersection(set(words[i]))
        unique= list(unique)
        
        counter=[]
        
        for letter in unique:
            for word in words:
                counter.append(tuple([word, letter, word.count(letter)])  )
                
        dic={}
        for i in range(0,len(counter)):
            if counter[i][1] in dic:
                if counter[i][2]<=dic[counter[i][1]] :
                    
                    dic[counter[i][1]] = counter[i][2]
            else:
                dic[counter[i][1]]= counter[i][2]
        
        out = []
        for letter in unique:
            out.extend([letter] * dic[letter])
    
        return out
     
a= Solution()
a.commonChars(words = ["bella","label","roller"])

a.commonChars(words = ["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"])


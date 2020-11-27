# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:19:23 2020

@author: kalan
"""

# =============================================================================
# 884. Uncommon Words from Two Sentences
# 
# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
# 
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# 
# Return a list of all uncommon words. 
# 
# You may return the list in any order.
# 
#  
# 
# Example 1:
# 
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
# 
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
#  
# =============================================================================


A = "this apple is sweet"
B = "this apple is sour"

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        s1 = A.split(' ')
        s2 = B.split(' ')
        
        dic ={}
        for word in s1:
            if word in dic:
                dic[word]+=1
            else:
                dic[word] = 0 
        
        for word in s2:
            if word in dic:
                dic[word]+=1
            else:
                dic[word] = 0 
        
        out=[]
        for key in dic:
            if dic[key] == 0 :
                out.append(key)        
                    
        return out

a=Solution()
a.uncommonFromSentences(A, B)
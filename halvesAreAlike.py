# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:35:49 2021

@author: kalan
"""

# =============================================================================
# 1704. Determine if String Halves Are Alike
# 
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# 
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# 
# Return true if a and b are alike. Otherwise, return false.
# 
# =============================================================================
 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.


1037
10:48

s='book'
s = "AbCdEfGh"
s = "MerryChristmas"
class Solution:
    def halvesAreAlike(self, s):
        
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        length = int(len(s)/2)
        
        first =s[0:length]
        
        sec= s[length:]
        
        cn=0
        for i in first:
            if i in vowels:
                cn+=1
        cnt=0
        for i in sec:
            if i in vowels:
                cnt+=1    
        
        if cn == cnt:
            return True
        else:
            return False
        
a=Solution()
a.halvesAreAlike(s)                            
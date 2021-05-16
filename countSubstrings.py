# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:51:23 2021

@author: kalan
"""
# 1638. Count Substrings That Differ by One Character
# Medium

# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.
# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.
# Return the number of substrings that satisfy the condition above.
# A substring is a contiguous sequence of characters within a string.
# Example 1:

# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.






# count = 0
# for i in range(len(s)):
    
#     for j in range(len(t)):
#         if strdif(s[i:i+1],t[j:j+1] )==1:
#             count+=1
#             #print(s[i:i+1],t[j:j+1])

#         if strdif(s[i:i+2],t[j:j+2] )==1:
#             count+=1
#             print(s[i:i+2],t[j:j+2])
            
#         if strdif(s[i:i+3],t[j:j+3] )==1:
#             count+=1
#             print(s[i:i+3],t[j:j+3])

s='aba'
t='baba'
res=0
for i in range(1,len(s)+1): 
   for j in range(len(s)-i+1):
       print(s[j:j+i])
       for k in range(len(t)-i+1):
           
           cnt = 0
           for x, y in zip(s[j:j+i], t[k:k+i]):
               
               if x != y:
                   cnt += 1
               if cnt > 1:
                   break
           if cnt <= 1 and cnt != 0:
               res += 1

    

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        

        def strdif(s,t):
            if len(s) != len(t):
                return 0
            else:
                
                cntr=0
                for i in range(len(s[0:3])):
                    if i < len(t):
                        
                        if s[i] != t[i]:
                            cntr+=1 
                return cntr
        
        
        im =[]
        for i in range(len(s)): 
           for j in range(i,len(s)):
               im.append(s[i:j+1])
             
        sec=[]
        for k in range(len(t)):
            for l in range(k,len(t)):
                sec.append(t[k:l+1])
        
        count=0          
        for i in im:
            for j in sec:
                if len(i)==len(j):
                    if strdif(i,j) ==1:
                        count+=1
        
        return count
    
a=Solution()
a.countSubstrings(s, t)

a.countSubstrings("ab","bb")
#only case where it doesn't work!
a.countSubstrings("abbab", "bbbbb")
-----
a.countSubstrings(s = "abe", t = "bbc")
a.countSubstrings(s = "a", t = "a")


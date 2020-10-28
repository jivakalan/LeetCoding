# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:54:54 2020

@author: kalan
"""

# =============================================================================
#1002. Find Common Characters
# Example 1:
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# =============================================================================


##create a dictionary with all letters in alphabet 

import string
alphabet = dict.fromkeys(string.ascii_lowercase, 0)

nums= ["bella","label","roller"]

l=[]
for letter in alphabet:
        
    for i in range(len(nums)):
        print(nums[i].count(letter))
        cnt= nums[i].count(letter)
        if alphabet[letter]>=3:
            alphabet[letter]=3
        else:
            
            alphabet[letter] += cnt
        

dic = {}
for letter in nums[0]:
    if letter in dic:
        continue
    cnt = nums[0].count(letter)
    for item in A:
        cnt = min(cnt, item.count(c))
        if cnt == 0:
            break
    if cnt != 0:
        dic[c] = cnt
res = []
for c, cnt in dic.items():
    res.extend([c] * cnt)

            
        
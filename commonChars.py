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
words=["cool","lock","cook"]

unique = list(set(words[0]).intersection(set(words[1])).intersection(set(words[2])))

counter=[]
for letter in unique:
    for word in words:
        thistuple= ( word, letter, word.count(letter) )
        counter.append(tuple([word, letter, word.count(letter)])  )



#output min of each unique element
cnt=0
for i in range(0,len(counter)):
    print(counter[i][2],counter[i][1])
    
##create a dictionary with all letters in alphabet 

import string
alphabet = dict.fromkeys(string.ascii_lowercase, 0)

nums= ["bella","label","roller"]


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
import string
alphabet = dict.fromkeys(string.ascii_lowercase, 0)

words = ["bella","label","roller"]

words=["cool","lock","cook"]

unique = list(set(words[0]).intersection(set(words[1])).intersection(set(words[2])))


counter=[]

for letter in unique:
    for word in words:
        counter.append(tuple([word, letter, word.count(letter)])  )

#output min of each unique element
import pandas as pd 

df=pd.DataFrame(columns=['letter','count'])

for i in range(0,len(counter)):
    
    df= df.append({ 'letter': counter[i][1] , 'count': counter[i][2] } 
                  , ignore_index=True  )


ab= df.groupby(['letter'])['count'].min()

out = []
for letter in unique:
    out.append(letter* ab[letter])
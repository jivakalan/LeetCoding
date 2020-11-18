# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:53:25 2020

@author: kalan
"""

#1078. Occurrences After Bigram
#Easy

# =============================================================================
# Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
# 
# For each such occurrence, add "third" to the answer, and return the answer.
# 
#  
# 
# Example 1:
# 
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]
# Example 2:
# 
# Input: text = "we will we will rock you", first = "we", second = "will"
#Output: ["we","rock"]
# =============================================================================


10:51
text = "alice is a good girl she is a good student"
text_l = text.split()
first = "a"
second = "good"

firs= first+' '+ second

dic={}
for i in range(0,len(text_l)):
    print(text_l[i]==first, text_l[i+1])
    if text[i] == first:
        dic[first]=text_l[i+1]






class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
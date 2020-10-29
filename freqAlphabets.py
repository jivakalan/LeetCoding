# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 00:33:49 2020

@author: jkalan
"""

# =============================================================================
# 1309. Decrypt String from Alphabet to Integer Mapping
# Easy
# 
# 399
# 
# 41
# 
# Add to List
# 
# Share
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
# 
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Return the string formed after mapping.
# 
# It's guaranteed that a unique mapping will always exist.
# 
#  
# =============================================================================

   
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
         
        import string 
        
        i=1
        alphabet={}
        for letter in string.ascii_lowercase:
            alphabet[i]=letter
            i+=1
        
        
# =============================================================================
#         for value in alphabet:
#             print(alphabet[value])
#             if alphabet[value]>=10:
#                 alphabet[value] = str(alphabet[value])+'#'
# =============================================================================
        

        out=[]
        i=0
        while i < len(s):
            #
            if i+2 < len(s) and s[i+2]=='#':
                out.append(alphabet[int(s[i:i+2])])
                i=i+3
            else:
                out.append(alphabet[int(s[i])])
                i=i+1
        
        outsr=''.join(out)
        return outsr



a=Solution()
a.freqAlphabets(s = "10#11#12")
a.freqAlphabets(s = "1326#")
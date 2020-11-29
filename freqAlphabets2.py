# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:04:50 2020

@author: kalan
"""
# =============================================================================
# 1309. Decrypt String from Alphabet to Integer Mapping
# 
# =============================================================================
# =============================================================================
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
# 
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# 
# Example 1:
# 
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:
# 
# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"
# 
# =============================================================================

#12:20:12:33

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l' ,'13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y', '26#':'z'     }     
                
        out=''
        
        for i in range(0,len(s)):
            if i+2 < len(s) and s[i+2]=='#':
                print(s[i:i+3])
                out= out+alphabet[s[i:i+3]]        
            else:
                out=out+ alphabet[s[i]]        
            
        return out

a=Solution()
a.freqAlphabets(s = "10#11#12")

a.freqAlphabets(s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")


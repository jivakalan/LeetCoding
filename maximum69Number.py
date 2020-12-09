# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:28:11 2020

@author: kalan
"""

# =============================================================================
# 1323. Maximum 69 Number
# 
# Given a positive integer num consisting only of digits 6 and 9.
# 
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
# 
#  
# 
# Example 1:
# 
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.
# Example 2:
# 
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:
# 
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
# 
# num=9669
# =============================================================================

class Solution:
    def maximum69Number (self, num: int) -> int:
        
        
        out = []
        for i in str(num):
            out.append(int(i))

        #only change the first 6 you see 
        if 6 in out:
            n=0
            while n<1:

                for i in range(0,len(out)):

                    if out[i]== 6:
                        out[i]= 9
                        n=99
                        break

                    continue     
        
            outs = [str(i) for i in out]          
            out= int(''.join(outs))
    
            return out
        else:
            return num
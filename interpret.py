# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:49:10 2020

@author: kalan
"""

# =============================================================================
# 1678. Goal Parser Interpretation
# 
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# 
# Given the string command, return the Goal Parser's interpretation of command.
# 
#  
# 
# Example 1:
# 
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:
# 
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:
# 
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
# 
# 
# =============================================================================

7;28
7:39 ---TYPO I DIDNT SPOT.....
command = "G()(al)"
command = "G()()()()(al)"

command = "(al)G(al)()()G"


#brute force




class Solution:
    def interpret(self, command):
        
        out=''
        i=0
        while i < len(command):
        
                if command[i]=='G':
                    out = out + 'G'
                    i+=1
            
                if i+1 < len(command):  
                    if command[i+1] == ')':
                        print(command[i])
                        out = out + 'o'
                        i+=2
                
                if i+1 < len(command):        
                    if command[i+1]=='a':
                        out = out + 'al'
                        i+=4
        return out
           

a=Solution()
a.interpret(command)
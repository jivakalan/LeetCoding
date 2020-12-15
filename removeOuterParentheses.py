# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:11:43 2020

@author: kalan
"""

1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


# =============================================================================
# Example 1:
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = 
#"()()()()(())".
# ()()()()(())'
# Example 3:
# 
# Input= "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# =============================================================================


init =  "(()())(())"
decomposition = "(()())" + "(())".
removeouter=  "()()" + "()" = "()()()".

init="(()())(())(()(()))"
decomp = (()())  + (())  + (()(()))
remove outer = () () + () +  ()(())

class Solution:
    def removeOuterParentheses(self, init):
       #decompose!             
        cnt =0   
        startidx=0
        out=''      
        for idx,char in enumerate(init):
            print(idx,char)
            if char =='(':
                cnt+=1
            if char ==')':
                cnt=cnt-1
            if cnt == 0:
                print(cnt)
                print(startidx,idx)
                out= out + init[startidx+1:idx]
                startidx=idx+1
        return out

a=Solution()
a.removeOuterParentheses(init="(()())(())(()(()))")
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
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
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

init ='(()())' 
(())
121210 1210


for i in range(0,len(init)):
    if i+1 < len(init):
        
        if init[i]=='(' and init[i+1] != ')':
        #FIND IT'S CLOSING PARTNER IF IT IS NOT RIGHT NEXT TO IT 
            #iterate through i+2...to end
            for nxet in range(i+1,len(init)):
                if init[nxet] ==')' and init[nxet-1]==')':
                    init=init[i+1:]
                    init=init[:nxet-1]

                    


        
    cnt = 0
    for n in range(0,len(init)):
        if n+1 < len(init):
            
            


##decompose
cnt=0
for i in range(0,len(nums)) :
    
    if nums[i]=='(':
        cnt+=1
        start = i
        #print(i,cnt)
    if nums[i]==')':
        cnt= cnt-1
        #print(i,cnt)
    if cnt ==0:
        out = nums[start:i]
        print(start,i)

##remove outer paranthesis
for i in out:
    if i=="(":
        out= out.replace(i,'')
    if i ==")":
        out= out.replace(i,'')
        
       

out=''

for i in range(0,len(Input)):
    if i+1 < len(Input):
        
        if Input[i]=='(' and Input[i+1]==')':
            out=out+'()'

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
       
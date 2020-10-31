# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:28:22 2020

@author: kalan
"""

#1614 1614. Maximum Nesting Depth of the Parentheses
#Easy


s = "(1+(2*3)+((8)/4))+1"

s="1"

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        out=[]
        for i in s:
            if i == '(':
                cnt+=1
                out.append(cnt)
            if i ==')':
                cnt-=1
                out.append(cnt)
      
        if not out:
            res=0
        else:
            res= max(out)
        return res
    
a=Solution()
a.maxDepth(s = "1")
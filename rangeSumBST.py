# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:32:57 2020

@author: kalan
"""
# =============================================================================
# 
# 938. Range Sum of BST
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
# 
#  
# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# 
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# =============================================================================
# =============================================================================
# Constraints:
# 
# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are uniqu
# =============================================================================


10:14
10:35

10:36 youtube

root=[10,5,15,3,7,None,18]

low = 7
high = 15


class Solution(object):
    def rangeSumBST(self, root, L, R):
        
             
        sum=0
        for i in root:
            if i:
                
                if i>=low and i<=high:
                    sum+=i
        return sum

a=Solution()
a.rangeSumBST(root,low,high) 



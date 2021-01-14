# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:18:22 2021

@author: kalan
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        

        
        if root.node == val:
            return root
        
        if root.node > val:
            self.searchBST(root.left, val)
        
        if root.node < val:
            self.searchBST(root.right, val)
        
        
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:55:09 2021

@author: kalan
"""

# =============================================================================
# 1315. Sum of Nodes with Even-Valued Grandparent
# Medium
# 
# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
# 
# If there are no nodes with an even-valued grandparent, return 0.
# Example 1:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
# =============================================================================


#solved--
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def insert(self, newval):
        
        if newval < self.val:
            if self.left is None:
                self.left = TreeNode(newval)
            else:
                self.left.insert(newval)
        if newval > self.val:
            if self.right is None:
                self.right = TreeNode(newval)
            else:
                self.right.insert(newval)   
                



root = TreeNode(val=5)
root.insert(3)
root.insert(6)
root.insert(2)
root.insert(4)
root.insert(1)
root.insert(8)
root.insert(7)
root.insert(9)


class Solution:
    
    def sumEvenGrandparent(self, root):
        self.res=0
        
        def inOrder(root, parent = 1, gparent =1):            
            if root:
                if gparent % 2 == 0:
                    self.res+= root.val
                    print(gparent)
    
                inOrder(root.left, root.val, parent)
               # print(root.val, gparent)
                inOrder(root.right, root.val, parent)
                
        inOrder(root)
        
        return self.res
            
    
a=Solution()
a.sumEvenGrandparent(root)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
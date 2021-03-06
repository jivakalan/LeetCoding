# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:38:07 2021

@author: kalan
"""

# =============================================================================
# 897. Increasing Order Search Tree
# Easy
# 
# =============================================================================
# Share
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
# 
#  
# 
# Example 1:
# 
# 
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:
# 
# 
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
# =============================================================================


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        #why does this self.left and slef.right exist? shoudl they not be Nodes themselves...
        
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
                
root = TreeNode(val=5, left =3, right =6)
        
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
    def increasingBST(self, root):
        
        def inOrder(root,result):
            if not root:
                return None
            
            inOrder(root.left, result)
            result.append(root.val)
            inOrder(root.right, result)

            return result
        
        result = []
        out = inOrder(root, result)
         
        return out

                
a=Solution()
out =a.increasingBST(root)            
            
            
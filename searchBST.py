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


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.val = data

# Insert method to create nodes
    def insert(self, data):

        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree()


root = Node(4)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)

root.val

class Solution:
    def searchBST(self, root,val):
        
        if root.val == val:
            return root
        
        if root.val > val:
            self.searchBST(root.left, val)
        
        if root.val < val:
            self.searchBST(root.right, val)
            
        
a=Solution()
val=2
a.searchBST(root, val)        
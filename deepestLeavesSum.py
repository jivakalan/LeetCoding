# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:51:44 2021

@author: kalan
"""

# =============================================================================
# 1302. Deepest Leaves Sum
# Medium
# 
# Given a binary tree, return the sum of values of its deepest leaves.
#  
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# =============================================================================


# Definition for a bi

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


root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)

def deepestleaf(root):
    out=[]
    if root.left:

        deepestleaf(root.left)
        out=root.left.val
    #print(out, root.left.val)
        
    return out  
out1 = deepestleaf(root)    
def deepest_rleaf(root):
    out=[]
    if root.right:

        deepestleaf(root.right)
        out=root.right.val
  
    return out  
out2 = deepest_rleaf(root)  

out = out1+out2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
           

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def deepestleaf(root):
            out=[]
            if root.left:
        
                deepestleaf(root.left)
                out=root.left.val
            #print(out, root.left.val)
                
            return out  
            
        def deepest_rleaf(root):
            out=[]
            if root.right:
        
                deepestleaf(root.right)
                out=root.right.val
          
            return out  
        out1 = deepestleaf(root)
        out2 = deepest_rleaf(root)  
        out = out1+out2
        return out            

a=Solution()
a.deepestLeavesSum(root)
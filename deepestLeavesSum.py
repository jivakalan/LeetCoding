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



# Definition for a binary tree node.
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
                

root = TreeNode(
[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5])        


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
    
    def deepestLeavesSum(self, root):
        
        #find max depth 
        def findmaxRDepth(root, cnt):
            if root is not None: 
            #first find deepest node on left-sub tree
                findmaxRDepth(root.left,cnt)    
                cnt.append(root.val)
              
        def lDepth(root, cnt):
            if root is not None: 
            #first find deepest node on right-sub tree
                lDepth(root.right,cnt)    
                cnt.append(root.val)
    
            
        
        cntL = []
        findmaxRDepth(root,cntL)
        cntr=[]
        lDepth(root,cntr)
        
        deepsum = cntL[0]+cntr[0]
        return deepsum
        #get the deepest value on each side and add it up
        



a=Solution()
a.deepestLeavesSum(root)














class Solution:
    
    def deepestLeavesSum(self, root):
        
        def deepsum(root):
            
            if not root:
                return None
            
            print(root.left.val,root.right.val)
            deepsum(root.left)
               # deepsum(root.right)
                

    
    
a=Solution()
a.deepestLeavesSum(root)
#












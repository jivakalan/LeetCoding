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
        #hard coded maxDepth for testing
        #maxDepth = 3
        
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
        maxDepth = max(len(cntL), len(cntr))

        dic={}
        def dfs(root,depth):
           # if root is not None:
            if depth in dic:
    
                dic[depth] += root.val
            else:
                dic[depth] = 0
                dic[depth] += root.val

            if depth+1< maxDepth:
                if root.left:
                    dfs(root.left, depth+1)
                if root.right:
                    dfs(root.right, depth+1)

        
        dfs(root, depth=0)
        return dic[maxDepth-1]




a=Solution()
a.deepestLeavesSum(root)

root = TreeNode(val=37)
root.insert(97)
root.insert(18)
root.insert(19)
root.insert(25)



class Solution:
    
        
    def deepestLeavesSum(self, root):
        
        #find max depth 
        def findmaxRDepth(root, cnt):
            
            if root is not None: 
            #first find deepest node on left-sub tree
                findmaxRDepth(root.left,cnt)   
                if root.val != node:
                    
                    findmaxRDepth(root.right, cnt)
                cnt.append(root.val)
        
              
        def lDepth(root, cnt):
            if root is not None: 
            #first find deepest node on right-sub tree
                lDepth(root.right,cnt) 
                if root.val != node:
                    lDepth(root.left,cnt)
                cnt.append(root.val)
        
                
        cntL = []
        node = root.val
        findmaxRDepth(root,cntL)
        
        cntr=[]
        node = root.val
        lDepth(root,cntr)
        maxDepth = max(len(cntL), len(cntr))
        
            
    
        dic={}
        def dfs(root,depth):
           # if root is not None:
            if depth in dic:
    
                dic[depth] += root.val
            else:
                dic[depth] = 0
                dic[depth] += root.val
    
            if depth+1< maxDepth:
                if root.left:
                    dfs(root.left, depth+1)
                if root.right:
                    dfs(root.right, depth+1)
    
        
        dfs(root, depth=0)
        return dic[max(dic, key=int)]

a=Solution()
a.deepestLeavesSum(root)
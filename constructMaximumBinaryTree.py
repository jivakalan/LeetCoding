# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:38:52 2021

@author: kalan
"""

# 654. Maximum Binary Tree
# Medium

# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums





class TreeNode:
  #initialize the attributes of the node
  def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None  

class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        def insert(root, data):
                if root.left is None:
                    root.left = TreeNode(data)
                else:
                    insert(root.left, data)
        def r_insert(root, data):
                if root.right is None:
                    root.right = TreeNode(data)
                else:
                    r_insert(root.right, data)
        
        def maxtree(root, nums):
            
            l_arr = nums[0:nums.index(max(nums))]
            r_arr = nums[nums.index(max(nums))+1:]
                
            
            if l_arr: 
                insert(root,max(l_arr))
                maxtree(root.left, l_arr)
                
            if r_arr:
                r_insert(root, max(r_arr))
                maxtree(root.right, r_arr)
        
                
        root = TreeNode(max(nums))
        maxtree(root, nums)
        return root   
    
a=Solution()
root = a.constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
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


nums = [3,2,1,6,0,5]

root = TreeNode(max(nums))

for i in range(0, nums.index(max(nums))):
    l_arr = nums[0:nums.index(max(nums))]
    r_arr = nums[nums.index(max(nums))+1:]
    if l_arr:
      #insert to left  
        root.insert(max(l_arr))'
    if r_arr:
        #insert to right
        root.insert(max(r_arr))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
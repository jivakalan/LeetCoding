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
    def rangeSumBST(self, root: TreeNode, L, R):
        return self.helper(root, L, R, 0)
    
    def helper(self, node, left, right, total):
        if node is None:
            return total
    
        if left <= node.val <= right:
        #if the node value is within the range then add it to the total
            total+= node.val
            #once you've added to the total then traverse down the tree via the left sub-tree and recursively add all node values within the range to the total
            total= self.helper(node.left, left,right,total)
            #once you've added to the total, then traverse down the tree via the right sub-tree and recursively add all node values within the range to the total    
            total= self.helper(node.right,left,right,total)
        
        #what if the node value is not within the range, ex: 6 
        # you know that if the node value is below the range then the best option is to traverse the tree down the right because in a BST, values ot the right are going to be greater than values to the left
        if node.val < left:
            total = self.helper(node.right,left,right,total)
        #likewise, if the node value is not within the nrage, but is greater than the top of the range , i.e. 16 then the best course of actoin is to traverse the tree via the left  sub-tree because the structure of a BST guarantees that values to the left are less than values to the right
        #at best you have values that are less than the top of the range, at worst null..and move on
        if node.val > right:
            total = self.helper(node.left,left,right,total)
        
        return total
            
        
   
        
   
    
a=Solution()
a.rangeSumBST(root,low,high) 


#next exercise --learn to create the BST you know what it is now:)
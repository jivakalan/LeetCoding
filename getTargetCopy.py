# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:08:40 2021

@author: kalan
"""

# =============================================================================
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Medium
# 
# 
# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# 
# The cloned tree is a copy of the original tree.
# 
# Return a reference to the same node in the cloned tree.
# 
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
# 
# Follow up: Solve the problem if repeated values on the tree are allowed.
# 
#  
# 
# =============================================================================


class Solution:
    def getTargetCopy(self, original, cloned, target):
        

        def inOrder(cloned, target):
            
            if not cloned:
                return None
            
            inOrder(cloned.left,target)
            if cloned.val == target.val:
                
                self.ans= cloned.val
                
            inOrder(cloned.right, target)

        
          
        
        inOrder(cloned, target)
        return self.ans

original = root
cloned = root
target = root
        

a=Solution()
a.getTargetCopy(original, cloned, target)
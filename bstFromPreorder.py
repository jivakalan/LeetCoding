# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 12:33:47 2021

@author: kalan
"""

# 1008. Construct Binary Search Tree from Preorder Traversal
# Medium


# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

preorder = [8,5,1,7,10,12]
Output= [8,5,10,1,7,null,12]




  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        
        def insert(root, data):
            
            if data < root.val:
                if root.left:
                    insert(root.left, data)
                else:
                    root.left = TreeNode(data)
            if data > root.val:
                if root.right:
                    insert(root.right, data)
                else:
                    root.right = TreeNode(data)
        
        
        # def crawl(root,res):
            
        #     if not root: 
        #         return None
        #     else:
                
        #     #print(root.right.val)
        #         if not root.left:
        #             if not root.right:
        #                 return None
                
                        
        #         if not root.left:
        #             res.append("null")
                    
                    
        #         else:
        #             res.append(root.left.val)
                    
        #         if not root.right:
        #             res.append("null")
        #         else:
        #             res.append(root.right.val)
                
        #         crawl(root.left, res)
        #         crawl(root.right,res)
            
            
            
        #create the tree 
        root = TreeNode(preorder[0])     
            
        for i in range(1,len(preorder)):
            insert(root, preorder[i])
            ##CRAWLING WAS UNNECESARY
        
            
        # ##crawl the tree and insert into the output 
        # res=[]
        # res.append(root.val)
        # crawl(root,res) 
        
        return root 
    

a=Solution()
a.bstFromPreorder(preorder = [1,3])
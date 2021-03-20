# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:06:45 2021

@author: kalan
"""

# =============================================================================
# 590. N-ary Tree Postorder Traversal
# Easy
# 
# 
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# 
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
# 
#  
# 
# Example 1:
# 
# =============================================================================





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children


        
n0 = TreeNode(val=1)
n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)

n0.children = [n1,n2,n3]
n1.children = [n4,n5]

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:






class Solution:
    def postorder(self, n0):
        
        out =[]
        for i in range(0,len(n0.children)):
            if n0.children[i].children:
                
                for j in range(0,len(n0.children[i].children)):
                #    print(n0.children[i].children[j].val)
                    out.append(n0.children[i].children[j].val)
                
           # print(n0.children[i].val)
            out.append(n0.children[i].val)
        #print(n0.val)
        out.append(n0.val)
        
        return out
    
a=Solution()
a.postorder(n0)




Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

[2, 6, 7, 3, 4, 9, 10, 5, 1]

n0 = TreeNode(val=1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)

n5 = TreeNode(6)
n6 = TreeNode(7)

n7 = TreeNode(8)

n8= TreeNode(9)
n9= TreeNode(10)
n10= TreeNode(11)

n11= TreeNode(12)
n12= TreeNode(13)
n13= TreeNode(14)

n0.children = [n1,n2,n3,n4]
n2.children = [n5,n6]
n3.children = [n7]
n4.children = [n8,n9]
n6.children = [n10]
n7.children = [n11]
n8.children = [n12]

n10.children =[n13]

root = n0






class Solution:
    def postorder(self, root):
        
        out =[]
        for i in range(0,len(root.children)):
            if root.children[i].children:
                
                for j in range(0,len(root.children[i].children)):
                    print(n0.children[i].children[j].val)
                    out.append(root.children[i].children[j].val)
                
           # print(n0.children[i].val)
            out.append(root.children[i].val)
        #print(n0.val)
        out.append(root.val)
        
        return out

a=Solution()
a.postorder(root)
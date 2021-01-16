# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:18:22 2021

@author: kalan
"""


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
root.PrintTree()

class Solution:
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree()
            
    def searchBST(self, root,val):
        
        if root == None:
            return None
        
        
        
        if root.val == val:
            #print(root.val.PrintTree())
            return root

        
        if root.val > val:
            return self.searchBST(root.left, val)
            
        
        if root.val < val:
            return self.searchBST(root.right, val)
       
        
a=Solution()

out = a.searchBST(root, 2)        
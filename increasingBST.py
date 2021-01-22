# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:35:26 2021

@author: kalan
"""

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


root = Node(5)
root.insert(3)
root.insert(6)
root.insert(2)
root.insert(4)
root.insert(8)
root.insert(1)
root.insert(7)
root.insert(9)

root.PrintTree()


class Solution:
    
    def increasingBST(self, root):
        out=[]
        if root is None:
            return None
        
        if root.left:d
           
            self.increasingBST(root.left)
        out.append(root.val),
        
        
       
        if root.right:
            self.increasingBST(root.right)
            
        return out
       
    

a=Solution()
a.increasingBST(root) 




#left, left ,left --if last left, then work your way up - if right, exists, then node and right,     
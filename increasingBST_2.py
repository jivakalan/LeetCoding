

class Tweet:
    def __init__(self, message):
        self.message = message

a=Tweet('hi') ##instance object created "a"
a.message
#instance objects inherits characteristics of their class

a.message ='140 characters'  #assign string ot the instance attribute, "message"

print(a.message)
print(Tweet.message)


##methods with __ are special "hooks" in python; "dunder" methods -duner =="double underscore" 
##dunder init = constructor or initializer method and is called AUTOMATICALLY when an instance is created


#must use self as the first parameter in dunder init method--why? 








class Node:
    #initialize the attributes of the node
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                #if the new value is less than node value, goes to the left 
                self.left = Node(data)
            else:
                self.left.insert(data)
                
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right = data
            
root = Node(5)
root.insert(3)
root.insert(7)
root.insert(1)






class Solution:
    
    def increasingBST(self, root):
        
        
        def inOrder(root,res):
            if not root:
                return None
            #inorder Traversal
          #  if root.left:

            inOrder(root.left, res)
            res.append(root.data)
            inOrder(root.right,res)
            
            return res
        
        #out = Node(inOrder(root,[]))
        res= inOrder(root,[])
        
        return res
            
a=Solution()
out= a.increasingBST(root)

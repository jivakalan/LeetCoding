# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:08:27 2021

@author: kalan
"""

# 1769. Minimum Number of Operations to Move All Balls to Each Box
# Medium


# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

 

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
# Example 2:

# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
import time





class Solution:
    def minOperations(self, boxes: str) :
        
        answer={}
        for i in range(0,len(boxes)):
            answer[i]=0
        
        for i in range(0,len(boxes)):
            for j in range(0,len(boxes)):         
                if boxes[j] == '1' and i != j :
                    
                    #print(i,j,  boxes[i], boxes[j])
                    
                    if i in answer:
                        
                        answer[i] += abs(j-i)
                    else:
                        answer[i] = 0
                        answer[i] += abs(j-i)
        
        if len(boxes)> 1:
            return list(answer.values())
        else:
            return [0]
                            
       


a=Solution()
a.minOperations(boxes = "110")
a.minOperations(boxes = "001011")
a.minOperations(boxes = "0")
a.minOperations(boxes = "1000")

start =time.time()
a.minOperations(boxes = "1000")
# a.minOperations(boxes ="01010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101")

stop = time.time()
print(stop-start,'seconds elapsed')



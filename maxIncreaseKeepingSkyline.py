# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:32:44 2021

@author: kalan
"""

# =============================================================================
# #+10mins
# 807. Max Increase to Keep City Skyline
# Medium
# 
# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
# 
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
# 
# What is the maximum total sum that the height of the buildings can be increased?
# 
# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: 
# The grid is:
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
# 
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
# 
# The grid after increasing the height of buildings without affecting skylines is:
# 
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
# 
# 
# 
# =============================================================================
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

cnt=0

for x in range(0,len(grid)):
    row_max = max(grid[x])
    x = 2
    
    print(x)
    print(grid[:x])

    print(grid[:x]+grid[x+1:])
    
    grid[~x]
    for y in range(0,len(grid[x])):
        if grid[x][y] != row_max:
            
            while grid[x][y] < row_max-1:
            
                
                
                grid[all elements except wherelement ==row_max] +=1
                
        else:
            continue

            
        
        
class Solution:
    def maxIncreaseKeepingSkyline(self, grid): #: List[List[int]]) -> int:
        cnt=0
        for x in range(0,len(grid)):
            row_max = max(grid[x])

            for y in range(0,len(grid[x])):

                while grid[x][y] < row_max:
                    grid[x][y]+=1
                    cnt+=1
                else:
                    continue
        return cnt
        
        
a=Solution()
a.maxIncreaseKeepingSkyline(grid=[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
        
        
        
        
        
        
        
        
        
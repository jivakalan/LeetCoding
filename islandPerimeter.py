# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:08:13 2020

@author: jkalan
"""

# =============================================================================
# 463. Island Perimeter
# Easy
# 
# 
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 
# represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by
# water, and there is exactly one island (i.e., one or more connected land cells).
# 
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the 
# island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
#Determine the perimeter of the island.
# Example 1:
# 
# 
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:
# 
# Input: grid = [[1]]
# Output: 4
# Example 3:
# 
# Input: grid = [[1,0]]
# Output: 4
# =============================================================================



grid = [[0,1,0,0]
       ,[1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]


grid=[[1,0]]

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        import numpy as np
        grid = np.array(grid)
        
        
        rows = grid.shape[0]
        cols = grid.shape[1]
        perimeter =0 
        
        for x in range(0,rows):
            for y in range(0,cols):
                
                
                if grid[x,y]==1 :
                    #print(x,y)
                    
                    perimeter +=4 
                    #print('perimeter is:', perimeter)
                   # print(x,y-1)
                    if (y-1)>=0 and grid[x,y-1]==1:
                        
                        perimeter = perimeter -2
                        #print('left',perimeter)
                    if (x-1)>=0 and grid[x-1,y]==1:
                       
                        perimeter = perimeter -2
                        #print('above',perimeter)
                    
        return perimeter
    
    
a= Solution()
a.islandPerimeter(grid)

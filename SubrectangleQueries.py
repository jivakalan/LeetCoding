# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:49:33 2021

@author: kalan
"""
8:11
8:27 --update done!
--next must...implemement get Value
--done --took 30 seconds
8:49-8;55
--just working the class..questions remains -- how to use the constructor correctly to init the rectangle??
--can i use numpy or not? 
# =============================================================================
# 1476. Subrectangle Queries
# 
# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
    # Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and                 bottom right coordinate is (row2,col2).



# 2. getValue(int row, int col)
    # Returns the current value of the coordinate (row,col) from the rectangle.



# Constraints:
# 
# There will be at most 500 operations considering both methods: updateSubrectangle and getValue.
# 1 <= rows, cols <= 100
# rows == rectangle.length
# cols == rectangle[i].length
# 0 <= row1 <= row2 < rows
# 0 <= col1 <= col2 < cols
# 1 <= newValue, rectangle[i][j] <= 10^9
# 0 <= row < rows
# 0 <= col < cols
# =============================================================================



class SubrectangleQueries:
    import numpy as np


    def __init__(self, rectangle):
        
        self.rectangle = np.random.rand(5,3)
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for x in range(row1, row2+1):
            for y in range(col1, col2+1):
                self.rectangle[x-1,y-1] = newValue
        return self.rectangle 

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row,col]
        

obj = SubrectangleQueries(rectangle= np.random.rand(5,3))
obj.updateSubrectangle(row1=2,col1=1,row2=4,col2=3,newValue=7)
param_2 = obj.getValue(row=1,col=1)

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
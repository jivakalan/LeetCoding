# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:16:32 2021

@author: kalan
"""

1329. Sort the Matrix Diagonally
Medium

928

152

Add to List

Share
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]



for i in range(0, len(mat)):
               print(i)
    for x in i:
        print(i,x)
        
        
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
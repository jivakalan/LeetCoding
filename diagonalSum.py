# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 01:24:22 2020

@author: kalan
"""


1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
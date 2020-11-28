# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:54:41 2020

@author: kalan
"""

# =============================================================================
# 1351. Count Negative Numbers in a Sorted Matrix
# 
# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
# 
# Return the number of negative numbers in grid.
# 
#  
# =============================================================================
# =============================================================================
# 
# Example 1:
# 
# Input: grid = [[4,3,2,-1    ]
#               ,[3,2,1,-1   ]
#               ,[1,1,-1,-2  ]
#               ,[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
# 
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
# 
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
# 
# Input: grid = [[-1]]
# Output: 1
# 
# grid = [[-1]]
# grid = [[1,-1],[-1,-1]]
# =============================================================================



#brute force 0(m*n)
# log time? 
#break it in half...serach the right side...then left is the final # is also <0


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
                
        cnt=0
        for m in grid:
            for n in m:
                if n <0 :
                    cnt+=1
        return cnt

a=Solution()
a.countNegatives(grid)    
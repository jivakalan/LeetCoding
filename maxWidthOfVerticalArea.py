# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:50:11 2021

@author: kalan
"""

# =============================================================================
# 1637. Widest Vertical Area Between Two Points Containing No Points
# Medium
# 
# 
# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# 
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# 
# Note that points on the edge of a vertical area are not considered included in the area.
# 
#  
# 
# Example 1:
# 
# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:
# 
# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3
#  
# 
# Constraints:
# 
# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109
# =============================================================================


points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]



class Solution:
    def maxWidthOfVerticalArea(self, points):
                
        points.sort()
        out = []
        for x in range(len(points)):
        
            if x+1 < len(points):
                
               # print(points[x+1][0]-points[x][0] )
                out.append(points[x+1][0]-points[x][0])
                
        
        return max(out)

a=Solution()
a.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
a.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:22:35 2021

@author: kalan
"""

# 1828. Queries on Number of Points Inside a Circle
# Medium

# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

# Return an array answer, where answer[j] is the answer to the jth query.

 

# Example 1:


# Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
# Output: [3,2,2]
# Explanation: The points and circles are shown above.
# queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.

import math

class Solution:
    def countPoints(self, points, queries):
        
        
        out = []
        
        for cc in queries:
            cnt = 0
            for p in points:
             #   print(p)
              #  print(p, cc)
                # print((p[0]-cc[0])**2 ,(p[1]-cc[1])**2 , (cc[2])**2)
                
                #val = (p[0]-cc[0])**2 + (p[1]-cc[1])**2 - (cc[2])**2
                val = math.sqrt((p[0]-cc[0])**2 + (p[1]-cc[1])**2)
                
                # print(val, cc)
                
                
                if val <= cc[2]:
                #if val==0:
                    cnt+=1
                    
            out.append(cnt)
        return out 
    
a=Solution()
a.countPoints(points = [[1,3],[3,3],[5,3],[2,2]],queries = [[2,3,1],[4,3,1],[1,1,2]])
a.countPoints(points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])
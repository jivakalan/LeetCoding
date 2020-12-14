# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:01:49 2020

@author: kalan
"""

# =============================================================================
# 1266. Minimum Time Visiting All Points
# 
# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
# 
# You can move according to the next rules:
# 
# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.
#  
# 
# Example 1:
# 
# 
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
# Example 2:
# 
# Input: points = [[3,2],[-2,2]]
# Output: 5
# =============================================================================

points = [[1,1],[3,4],[-1,0]]
points = [[3,2],[-2,2]]

# =============================================================================
# cnt=0
# for i in range(0,len(points)):
#     if i+1 < len(points):
#         
#         init = points[i]
#         dest = points[i+1]
# 
# 
#         while dest[0]-init[0] < dest[1]-init[1]:
#                
#             #if x < y then move vertically
#             #move vertically
#             init[1] =  init[1]+1
#             cnt+=1
#             #have to move verticaly or horizontally
#         while dest[0]-init[0] > dest[1]-init[1]:
#             init[0] =  init[0]+1
#             cnt+=1
#         
#         while init != dest:
#             if dest[0]<0:
#                 init = [x-1 for x in init]
#             else:
#                 init = [x+1 for x in init]
#             cnt+=1
# return cnt
# =============================================================================



cnt=0

init = points[0]
dest = points[1]

while dest[0]-init[0] < dest[1]-init[1]:
       
    #if x < y then move vertically
    #move vertically
    init[1] =  init[1]+1
    cnt+=1
    #have to move verticaly or horizontally
while dest[0]-init[0] > dest[1]-init[1]:
    init[0] =  init[0]+1
    cnt+=1

while init != dest:
    if dest[0]<0:
        init = [x-1 for x in init]
    else:
        init = [x+1 for x in init]
    cnt+=1    


init = points[1]
dest = points[2]

while dest[0]-init[0] < dest[1]-init[1]:
       
    #if x < y then move vertically
    #move vertically
    init[1] =  init[1]+1
    cnt+=1
    #have to move verticaly or horizontally
while dest[0]-init[0] > dest[1]-init[1]:
    init[0] =  init[0]+1
    cnt+=1

while init != dest:
    if dest[0]<0:
        init = [x-1 for x in init]
    else:
        init = [x+1 for x in init]
    cnt+=1    







    
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        
        cnt=0
        for i in range(0,len(points)):
            if i+1 < len(points):
                
                init = points[i]
                dest = points[i+1]
        
        
                while dest[0]-init[0] < dest[1]-init[1]:
                       
                    #if x < y then move vertically
                    #move vertically
                    init[1] =  init[1]+1
                    cnt+=1
                    #have to move verticaly or horizontally
                while dest[0]-init[0] > dest[1]-init[1]:
                    init[0] =  init[0]+1
                    cnt+=1
                
                while init != dest:
                    if dest[0]<0:
                        init = [x-1 for x in init]
                    else:
                        init = [x+1 for x in init]
                    cnt+=1
        return cnt



a=Solution()
a.minTimeToVisitAllPoints()
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:01:49 2020

@author: kalan
"""

##testing commmit
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


points = [[3,2],[-2,2]]
points = [[1,1],[3,4][
    ],[-1,0]]
 
points = [[838,-127] ,[773,-917]]

            

#new algo 
3,2 
-2,2

three situations 
share (x coordinates) (2,3) & (2,8) --so just move vertically
share y coorindates  (2,3) & 8, 3) --so just move horizontally

share no coordinates 2,3 and (3,4)
    --must move in two steps
    --step 1 - move left or right OR up/down such that you share x/y coordinate


for i in range(0,len(points)):
    if i+1 < len(points):
        init = points[i]    # 1,1
        dest = points[i+1]  # 3,4


        #move from 1,1 to 3,4 (or move from 3,4 to -1,0
        #case 1 - move to 1,2 then diag
        #case 2- move diag all the way 

    
class Solution:
    def minTimeToVisitAllPoints(self, points):
        #
        cnt=0

        for i in range(0,len(points)):
            if i+1 < len(points):
                
                init = points[i]
                dest = points[i+1]
                
                
                
                
                while  dest[0]-init[0] != dest[1]-init[1]:
                    if abs(dest[1]-init[1]) > abs(dest[0]-init[0]) :
                        if dest[1] < init[1]:
                            init[1]=init[1]-1
                            cnt+=1    
                        else:
                            init[1]=init[1]+1
                            cnt+=1
                        
                        
                    else:
                        if dest[0]<init[0]:
                            
                            init[0]=init[0]-1
                            cnt+=1
                        if dest[0]>init[0]:
                            init[0]=init[0]+1
                            cnt+=1
                while init != dest :
                    
                    if dest[0]<init[0]:
                        init = [x-1 for x in init]
                    else:
                        init = [x+1 for x in init]
                    cnt+=1
            
        return cnt

a=Solution()
a.minTimeToVisitAllPoints(points)






points = [[3,2],[-2,2]]
points = [[1,1],[3,4]]
points =[[825,511],[932,618]]
 
i = 1
count = 0
while i < len(points):
    diff0 = points[i][0] - points[i-1][0]
    diff1 = points[i][1] - points[i-1][1]
   
    count += max(abs(diff0), abs(diff1))
    i+=1


#must revisit
#time limit exceeded -fixed
#now wrong answer! 
points =[[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]

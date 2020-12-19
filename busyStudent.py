# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:07:51 2020

@author: kalan
"""

1450. Number of Students Doing Homework at a Given Time

Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

 

Example 1:

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.

Input: startTime = [4], endTime = [4], queryTime = 4

Output: 1
Explanation: The only student was doing their homework at the queryTime.



startTime = [1,2,3] 
endTime = [3,2,7]
queryTime = 4

startTime = [1,1,1,1]
endTime = [1,3,2,4]
queryTime = 7

startTime = [9,8,7,6,5,4,3,2,1] 
endTime = [10,10,10,10,10,10,10,10,10] 
queryTime = 5

startTime = [4]
endTime = [4] 
queryTime = 4

cnt=0
for n in range(0,len(startTime)):
#    if endTime[n]- startTime[n] >= queryTime:
    if queryTime >= startTime[n] and queryTime <= endTime[n]:
        cnt+=1
        
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        

        cnt=0
        for n in range(0,len(startTime)):
        #    if endTime[n]- startTime[n] >= queryTime:
            if queryTime >= startTime[n] and queryTime <= endTime[n]:
                cnt+=1
        return cnt
    
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:52:37 2020

@author: kalan
"""

1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

    
Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


if n % 2 == 0:
    #if n is even 
    n/2 numbers such that n/2 == n
else:
    #if n is odd 
    n/2 numbers such that n/2 ==n and 0 in the middle 

#two cases 
n is odd, or n is even
if n is odd:
    (5)
   -y, -x,0, x, y
   (7)
   -z,-y,-x,0,x,y,z
   
if n is even (2) 
    -x,x   
    (4)
    -y,-x,x,y

n=2 2/2= 1
x = n
2,-2

n=4
n/2 = 2
2 DISTINCT numbers that add up to n
x,y = n-1 3 and n-(n-1) = 1
n=6
n/2 = 3
3 distinct numbers that add up to n
x + y + z = n



class Solution:
    def sumZero(self, n):
        out =[]
        #do some stuff
        
        #conditions
        sum(out) = 0
        len(out) = n
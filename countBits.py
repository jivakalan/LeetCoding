# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:46:47 2021

@author: kalan
"""

401. Binary Watch
Easy

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


hours = [1,2,4,8]
minutes = [1,2,4,8,16,32]


time=[]
for hours in range(0,13):
    for minutes in range(0,60):
        time.append((hours,minutes))

 def countBits(num):
        count = 0
        while num:
          count += num & 1
          num >>= 1
        return count
    
    
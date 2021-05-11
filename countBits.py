# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:46:47 2021

@author: kalan
"""

# 401. Binary Watch
# Easy

# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


##iterate through hours 0-11 and minutes 0-59


        
        

    
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        
        def countBits(num):
          count = 0
          while num:
            count += num & 1
            num >>= 1
          return count
        
        
        
        dic ={}
        for hour in range(0,12):
            for minute in range(0,60):
                #print(str(hour) + ":" + str(minute) )
                #print("%02d:%02d" %(hour, minute))
                
                #dic[str(hour) + ":" + str(minute)] = countBits(hour)+countBits(minute)
                dic["%d:%02d" %(hour, minute)]= countBits(hour)+countBits(minute)
        
        
        #turnedOn = 1
        count=0
        out = []
        #for i in dic.values():
            
        for key in dic:
            
            if dic[key] == turnedOn:
                count+=1
                out.append(key)
        return out 

a=Solution()
a.readBinaryWatch(turnedOn=1)
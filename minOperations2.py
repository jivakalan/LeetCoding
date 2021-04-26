# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:57:41 2021

@author: kalan
"""

# 1551. Minimum Operations to Make Array Equal
# Medium

# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.


class Solution:
    def minOperations(self, n):
        
        arr=[]
        for i in range(0,n):
            arr.append((2*i)+1)
        av=sum(arr)/len(arr)
        

             
                
        #use two pointers
        cnt=0
        for i in range(0,len(arr)):
            print(arr[i], arr[len(arr)-i-1])
            
            if arr[i] and arr[len(arr)-i-1] !=arr:

                cnt+=av-arr[i]
                arr[i]=av
                arr[len(arr)-i-1] = av
  

        return  cnt



a=Solution()
a.minOperations(n = 3)

a.minOperations(n = 6)

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:10:21 2020

@author: kalan
"""

1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
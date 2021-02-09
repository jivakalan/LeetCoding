# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:27:48 2021

@author: kalan
"""

1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

 

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
Example 2:

Input: n = "82734"
Output: 8
Example 3:

Input: n = "27346209830709182346"
Output: 9

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.


each digit is 1 or 0, no leading zeroes in the number

m=0
for x in n:
    x = int(x)
    print(x,m)
    m = max(x,m)
    
    int(n)


class Solution:
    def minPartitions(self, n: str) -> int:
        
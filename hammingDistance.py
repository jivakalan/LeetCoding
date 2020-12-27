# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:41:46 2020

@author: kalan
"""

461. Hamming Distance
To convert integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient and the remainder. Continue dividing the quotient by 2 until you get a quotient of zero. Then just write out the remainders in the reverse order.

Here is an example of such conversion using the integer 12.
First, let’s divide the number by two specifying quotient and remainder:


import math as m




def convtodec(num):
#    out=[]
    div= num
    if div == 0:
        quit
    else:
        div = m.floor(num/2)
        mod = (num % 2)
        print(div,mod)
        out.append(mod)
        convtodec(div)


out=[]
convtodec(12)
out.reverse()
a=out
out=[]
convtodec(1)


class Solution:
    def hammingDistance(self, x,y):
        
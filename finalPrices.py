# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:44:08 2020

@author: kalan
"""


# =============================================================================
# 
# 1475. Final Prices With a Special Discount in a Shop
# Easy
# 
# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item,
# receive discount equivalent to prices[j] 
#      j is the minimum index such that j > i 
#      and prices[j] <= prices[i]
#      or no discount at all
# 
# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
# 
#  
# 
# Example 1:
# 
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.
# 
# =============================================================================


prices = [8,4,6,2,3]

class Solution:
    def finalPrices(self, prices):
        
        out=[]
        for i in range(0,len(prices)):
        
            for j in range(0,len(prices)):
                
                if prices[i]>= prices[j] and j>i:
                    out.append(prices[i]-prices[j])
                    
                    break
                
                if  prices[i] <= prices[j] and j>= i:
        
                    if len(prices)-1 == j:
                        out.append(prices[i])
        return out 
            
    
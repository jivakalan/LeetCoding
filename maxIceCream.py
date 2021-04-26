# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:39:08 2021

@author: kalan
"""

# 1833. Maximum Ice Cream Bars
# Medium


# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# Note: The boy can buy the ice cream bars in any order.

 

# Example 1:

# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.



class Solution:
    def maxIceCream(self, costs, coins):
        

        costs.sort()
        cnt=0
        for i in range(0,len(costs)):
            coins = coins - costs[i]
            
            if coins >= 0:
                cnt+=1
                #print(coins,cnt)
            else:
                break
        return cnt

a=Solution()
a.maxIceCream(costs = [1,3,2,4,1] ,coins = 7)
a.maxIceCream(costs = [10,6,8,7,7,8], coins = 5)
a.maxIceCream(costs = [1,6,3,1,2,5], coins = 20)
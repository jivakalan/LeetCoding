# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:07:24 2021

@author: kalan
"""
# 1418. Display Table of Food Orders in a Restaurant
# Medium

# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

 

# Example 1:

# Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
# Explanation:
# The displaying table looks like:
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
# For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
# For the table 5: Carla orders "Water" and "Ceviche".
# For the table 10: Corina orders "Beef Burrito". 




orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]


 out=[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"]
 ,["3","0","2","1","0"]
 ,["5","0","1","0","1"]
 ,["10","1","0","0","0"]] 





# dic2={}
# for order in orders:
#     if order[1] in dic2:
#         if order[2] not in dic2[order[1]]:
#             dic2[order[1]][order[2]] = 1
#         else:
#             dic2[order[1]][order[2]] +=1
#     else:
#         dic2[order[1]]= {order[2]:1}


class Solution:
    def displayTable(self, orders):
        
        out = [[]]
        for order in orders:
            if order[2] in out[0]:
                continue
            else:
                out[0].append(order[2])
        
        out[0].sort()
        out[0]
        
        
        
        dic = {} 
        for order in orders :
            if order[1] in dic:
                continue
            else:
                dic[order[1]] = dict((k,0) for k in out[0])
        
            
        for order in orders:
            
            if order[1] in dic:
                for key in dic[order[1]]:
                    if key == order[2]:
                         dic[order[1]][order[2]]+= 1
                        
             
                
        out[0].insert(0,'Table')
        
        tables= []
        for i in dic.keys():
            tables.append(int(i))
        tables.sort()
        
        for i in range(0,len(tables)):
            tables[i] = str(tables[i])
            
        
        for key in dic:
            for lkey in dic[key]:
                dic[key][lkey] = str(dic[key][lkey])

        for i in tables:
            temparr= list(dic[str(i)].values())
            temparr.insert(0, i)
            out.append(temparr  )
            
        return out 


a=Solution()
a.displayTable(orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
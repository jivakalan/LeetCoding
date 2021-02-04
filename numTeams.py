# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 10:43:35 2021

@author: kalan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:15:45 2021

@author: kalan
"""

# =============================================================================
# 1395. Count Number of Teams
# Medium
# 
# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# 
# You have to form a team of 3 soldiers amongst them under the following rules:
# 
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
# 
# =============================================================================
 
# =============================================================================
# 
# Example 1:
# 
# Input: rating = [2,5,3,4,1]
# Output: 3
# We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
# 
# =============================================================================

rating = [2,5,3,4,1]

                    
arr=rating
memoGreater = {}
        
memoLesser = {}
length = len(arr) ##an

for i in range(length):
    memoGreater[i] = []
    memoLesser[i] = []
    
    for j in range(i+1, length):
        if arr[j] > arr[i]:
           # print(arr[j])
            memoGreater[i].append(j)
        elif arr[j] < arr[i]:
            memoLesser[i].append(j)

numTeams = 0
		# add the teams using the conditions specified
for i in range(length):
    for index in memoGreater[i]:
        print(memoGreater[i], index, memoGreater[index],len(memoGreater[index]))
        numTeams += len(memoGreater[index])
    for index in memoLesser[i]:
        numTeams += len(memoLesser[index])
      

class Solution:
    def numTeams(self, rating):
        
        arr=rating
        memoGreater = {}
                
        memoLesser = {}
        length = len(arr) ##an
        
        for i in range(length):
            memoGreater[i] = []
            memoLesser[i] = []
            
            for j in range(i+1, length):
                if arr[j] > arr[i]:
                   # print(arr[j])
                    memoGreater[i].append(j)
                elif arr[j] < arr[i]:
                    memoLesser[i].append(j)
        
        numTeams = 0
        		# add the teams using the conditions specified
        for i in range(length):
            for index in memoGreater[i]:
                numTeams += len(memoGreater[index])
            for index in memoLesser[i]:
                numTeams += len(memoLesser[index])
        
        return numTeams
    
a=Solution()
a.numTeams(rating)

rating =[922,108,1029,129,1215,2987,1505,1503,2125,2000,677,838,2560,2540,2251,1840,276,1062,1219,1061,131,2504,748,900,9,2445,41,2235,1725,2261,1008,437,2267,1128,2258,2851,1766,2913,1737,1655,1632,1295,1682,2020,2437,1345,2204,2758,2722,1553,568,2479,1806,830,158,1085,1723,2542,2585,2108,2064,1692,696,2919,901,2211,1380,2410,1440,1207,103,644,2736,1036,1381,1009,98,2349,2311,1947,1985,2779,1874,2008,320,1273,56,314,581,1856,1978,1139,490,668,1891,813,1412,867,1340,272,2078,882,2446,2380,88,444,2550,740,328,1930,1224,379,687,556,513,2684,1789,1509,991,2236,121,1434,447,2326,365,1882,67,569,856,468,1541,523,1262,2257,915,2931,283,2630,1138,1325,2314,2778,553,1442,2037,233,1363,2511,811,419,2489,779,2366,2947,2713,1842,300,1095,1708,1492,2592,2145,1999,1700,2001,315,253,1744,430,1327,2038,1740,2721,445,751,1267,2850,861,1443,2546,2041,472,1661,1838,265,2664,2753,1195,2434,1200,2918,66,70,670,226,1235,2971,2166,1540,2547,2957,1234,151,1677,1284,1322,1621,1093,1546,2579,1652,550,2300,521,1562,2784,155,2909,1922,392,448,415,1247,2956,470,117,428,2985,541,1522,1524,2333,2392,2210,642,391,1872,2872,2345,82,2101,2165,603,1966,998,1570,175,60,2237,136,178,652,231,2821,2292,104,215,2196,2051,1362,2152,1818,1970,450,2802,847,1735,1053,191,1955,1032,590,621,459,1143,1044,2623,212,2416,2810,495,2711,1118,2964,293,2573,2495,404,1040,1501,2932,1552,2140,1487,1346,2294,2189,1927,1441,2463,2448,1030,1438,669,586,720,868,606,2141,2638,2614,2952,1738,675,1395,2624,142,2740,485,120,897,1542,592,2830,1602,2175,1534,845,1109,1045,1969,1326,795,1612,808,1825,1236,1482,996,1817,2961,1125,1942,576,914,898,268,301,439,2098,527,2844,1190,2735,2025,2515,1161,2054,758,1649,1437,1559,918,87]


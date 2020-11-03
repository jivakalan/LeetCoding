# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:09:56 2020

@author: jkalan
"""


# =============================================================================
# 
# =============================================================================
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct 
#path going from cityAi to cityBi. Return the destination city, that is, the city without any path 
#outgoing to another city.
# 
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be 
#exactly one destination city.
# 
#  
# 
# Example 1:
# 
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:
# # 
# =============================================================================
# =============================================================================




paths = [["qMTSlfgZlC","ePvzZaqLXj"]
        ,["xKhZXfuBeC","TtnllZpKKg"]
        ,["ePvzZaqLXj","sxrvXFcqgG"]   
        ,["sxrvXFcqgG","xKhZXfuBeC"]
        ,["TtnllZpKKg","OAxMijOZgW"]]


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        newpath = paths[0][1]
        for i in range(0,len(paths)): 
            
            if i+1== len(paths):
                pathminus=paths[:i]
                
                for eachpath in pathminus:
                    if newpath == eachpath[0]:
                        newpath = eachpath[1]

                    else:
                        continue
            else:
                pathminus = paths[:i]+paths[i+1:]
                
                for eachpath in pathminus:
                    if newpath == eachpath[0]:
                        newpath = eachpath[1]
                    else:
                        continue

        return newpath
        
a=Solution()
res =a.destCity(paths)





newpath = paths[0][1]
for i in range(0,len(paths)): 
    
    if i+1== len(paths):
        pathminus=paths[:i]
        
        for eachpath in pathminus:
            if newpath == eachpath[0]:
                newpath = eachpath[1]

            else:
                continue
    else:
        pathminus = paths[:i]+paths[i+1:]
        
        for eachpath in pathminus:
            if newpath == eachpath[0]:
                newpath = eachpath[1]
            else:
                continue
            

# =============================================================================
# 
# paths = [["B","C"],["D","B"],["C","A"]]
# 
# paths = [["B","C"],["A","E"],["C","A"]]
# 
# paths = [["A","E"],["B","C"],["C","A"]]
# 
# paths = [["B","C"],["A","E"],["C","A"]]
# 
# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# 
# 
# 
# 
# =============================================================================
        
        
        
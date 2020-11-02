# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:09:56 2020

@author: jkalan
"""


# =============================================================================
# 
# 
# for i in range(0,len(paths)):
#     if i+1<len(paths):
#         if paths[i][1] == paths[i+1][0]:
#             continue
#         else:
#             paths[i+1][1]
# 
# 
# =============================================================================
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        out=""
        for i in range(0,len(paths)):
            if i+1<len(paths):
                if paths[i][1] == paths[i+1][0]:
                    out= paths[i+1][1]
        return out
    
a=Solution()
out=a.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])

paths = [["B","C"],["D","B"],["C","A"]]

paths = [["B","C"],["A","E"],["C","A"]]

paths = [["A","E"],["B","C"],["C","A"]]

paths = ["B","C"],["A","E"],["C","A"]
pathminus:  ["A","E"],["C","A"]
newpath: ["C"]

if c==E:
    whath appes
if c--C:
    


for i in range(0,len(paths)):
    newpath = paths[i][1]
    
    if i+1== len(paths):
        pathminus=paths[:i]
        restpath =paths[i:]
        for eachpath in pathminus:
            print(newpath,eachpath)
        
    else:
        pathminus = paths[:i]+paths[i+1:]
        for eachpath in pathminus:
            print(newpath,eachpath)
        
        
        
        for eachpath in pathminus:            
            
            if newpath == eachpath[0] :
                
                newpath = eachpath
                print(newpath, eachpath)
            else:
                print(newpath[1])

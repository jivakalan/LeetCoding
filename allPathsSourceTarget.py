# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:36:20 2021

@author: kalan
"""

# 797. All Paths From Source to Target
# Medium

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

# Example 1:


# Input: graph = [[1,2],[3],[3],[]] Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


graph = [[1,2],[3],[3],[]] 




class Solution:
    def allPathsSourceTarget(self, graph):
        queue = []

        for i in range(len(graph[0])):
            print(graph[0][i])
            queue.insert(i, [graph[0][i]])    
            
        for i in queue:
            i.insert(0,0)
            
        #start = 0 
        target = len(graph)-1
        
        
        #queue = [[0,1],[0, 2]]
        out=[]
        
        for i in queue:
            
            if i[-1]== target:
                out.append(i)
            else:
                i.append(graph[i[-1]][0])
                if i[-1]== target:
                    out.append(i)
        
        return out 
    
a=Solution()
a.allPathsSourceTarget(graph = [[1,2],[3],[3],[]] )
a.allPathsSourceTarget(graph = [[1],[]])
a.allPathsSourceTarget(graph = [[1,2,3],[2],[3],[]])
a.allPathsSourceTarget(graph = [[1,3],[2],[3],[]])

a.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]])
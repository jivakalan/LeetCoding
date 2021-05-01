# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:17:27 2021

@author: kalan
"""

# 1817. Finding the Users Active Minutes
# Medium

# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

# Return the array answer as described above.

 

# Example 1:

# Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
# Output: [0,2,0,0,0]
# Explanation:
# The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
# The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
# Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.


logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
     

        

class Solution:
    def findingUsersActiveMinutes(self, logs, k) :
        
           
        dic={}
        for i in range(0, len(logs)): 
            
            if logs[i][0] in dic:
                
                if logs[i][1] not in dic[logs[i][0]]:
                    dic[logs[i][0]].append(logs[i][1])
        
            else:
                dic[logs[i][0]] = [logs[i][1]]
                
                
                
                
        for key in dic:
            dic[key]= len(dic[key])
        
        values = list(set(dic.values()))
        
                
        dic2 ={}
        for i in values:
            if i in dic2:
                continue
            else:
                dic2[i] = 0
                
        for value in dic.values():
        
                dic2[value] +=1
        
            
        
        answers = [0]*k
        
        for key in dic2:
        
            answers[key-1] = dic2[key]
        
        return answers

a=Solution()
a.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]],k = 5)
a.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4)

        

# =============================================================================
# 1282. Group the People Given the Group Size They Belong To
# Medium
# 
# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
# 
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
# 
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# 
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
# 
#  
# groupSizes[1]=3 ---person 1 is in a group of size 3
# 
# 
# reutn a list of groups that each perosn i is in a group of s
# 
# Example 1:

# =============================================================================
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation: 
# 
# The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
# The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
# Example 2:
# =============================================================================
#=============================================================================






class Solution:
    def groupThePeople(self, groupSizes):
        
        
        #List[int]) -> List[List[int]]:

        dic={}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dic:
                dic[groupSizes[i]] = [i]
            else:
                dic[groupSizes[i]].append(i)
        
        result = []    
        
        for key in dic:
            length_of_list_in_dic = len(dic[key])
            #if the the length of list (value) is > key
            if length_of_list_in_dic > key:
                #walk through the array, in group sized incremements  and place that sublist in result set 
                start =  0
                while start < length_of_list_in_dic:
                    end = start+key
                    result.append(dic[key][start:end])
                    print(start, end)
                    start +=key 
            else:
            #otherwise just place the list into the resultset
                result.append(dic[key])
        return result 
    
a=Solution()

result = a.groupThePeople(groupSizes = [3,3,3,3,3,1,3])
        
result = a.groupThePeople(groupSizes = [2,1,3,3,3,2])

result = a.groupThePeople(groupSizes = [3,4,3,3,4,4,3,4,3,3])

result= a.groupThePeople(groupSizes= [2,2,1,1,1,1,1,1])

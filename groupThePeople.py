
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



                                            

groupSizes = [3,3,3,3,3,1,3]

dic={}
for i in range(len(groupSizes)):
    print('person', i, 'is in a group of size', groupSizes[i])
    dic[i]=groupSizes[i]

out=[]
for key in dic:
    intermed =[]
    value = dic[key]
    if len(intermed) < dic[key]:
        #print(len(intermed),dic[key],value)
        for key in dic:
            
            if dic[key]==value:
                while len(intermed) <dic[key]:
                    intermed.append(key)
                    print(len(intermed))

    
        

    

class Solution:
    def groupThePeople(self, groupSizes):
        
        #List[int]) -> List[List[int]]:


        
        
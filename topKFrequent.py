


# =============================================================================
# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# 
# Input: nums = [1], k = 1
# Output: [1]
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
# =============================================================================



nums = [2,2,3,1,1,1] 
k = 2
nums = [1]
k = 1

class Solution:
    def topKFrequent(self, nums,k):
        
        dic ={}
        
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                
                dic[i] = 1
        
        out=[]
        for w in sorted(dic, key=dic.get, reverse= True):      
            out.append(w)
        nout = out[0:k]
        return nout

dic.get


a=Solution()
a.topKFrequent(nums,k)



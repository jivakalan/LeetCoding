# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:03:47 2020

@author: kalan
"""

# =============================================================================
# 
# 349. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# =============================================================================

10:05
10:07

nums1 = [1,2,2,1] 
nums2 = [2,2]

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1s = set(nums1)
        nums2s = set(nums2)
        nums3s = nums1s.intersection(nums2s)
        return nums3s

a=Solution()
a.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])        
# Find the Difference of Two Arrays

"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""

from typing import *

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 = set(nums1)
        hash2 = set(nums2)
        answer0 = []
        answer1 = []
        
        for i in hash1:
            if i not in hash2:
                answer0.append(i)

        for i in hash2:
            if i not in hash1:
                answer1.append(i)

        return [answer0, answer1]
    

# Test 1:
nums1 = [1,2,3]
nums2 = [2,4,6]

solution = Solution()
result = solution.findDifference(nums1, nums2)
print(result)


# Test 2:
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

solution = Solution()
result = solution.findDifference(nums1, nums2)
print(result)
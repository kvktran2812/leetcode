# Increasing Triplet Subsequence

from typing import *


"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        smallest = [nums[0]] * n
        biggest = [nums[-1]] * n

        for i in range(2, n):
            if nums[i-1] < smallest[i-1]:
                smallest[i] = nums[i-1]
            else:
                smallest[i] = smallest[i-1]

        for i in range(n-3, -1, -1):
            if nums[i+1] > biggest[i+1]:
                biggest[i] = nums[i+1]
            else:
                biggest[i] = biggest[i+1]

        for i in range(1, n-1):
            if smallest[i] < nums[i] and nums[i] < biggest[i]:
                return True
                
        return False
    
# Test 1
nums = [1,2,3,4,5]
solution = Solution()
result = solution.increasingTriplet(nums)
print(result)

# Test 2
nums = [5,4,3,2,1]
solution = Solution()
result = solution.increasingTriplet(nums)
print(result)

# Test 3
nums = [2,1,5,0,4,6]
solution = Solution()
result = solution.increasingTriplet(nums)
print(result)
# Find Pivot index

"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = left[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + nums[i+1]

        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1
    

# Test 1:
nums = [1,7,3,6,5,6]

solution = Solution()
result = solution.pivotIndex(nums)
print(result)


# Test 2:
nums = [1,2,3]

solution = Solution()
result = solution.pivotIndex(nums)
print(result)


# Test 3:
nums = [2,1,-1]

solution = Solution()
result = solution.pivotIndex(nums)
print(result)
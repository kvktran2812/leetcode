# Product of array except self

from typing import *
from math import *

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = 0
        idx = -1
        pre = 1
        ret = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
                idx = i
            else:
                pre *= nums[i]

        if zeros == 1:
            ret[idx] = pre
            return ret

        if zeros > 1:
            return ret

        for i in range(n):
            ret[i] = pre // nums[i]

        return ret
    

# Test 1:
nums = [1,2,3,4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result) # [24, 12, 8, 6]

# Test 2:
nums = [-1,1,0,-3,3]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result) # [0, 0, 9, 0, 0]
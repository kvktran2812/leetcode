# Maximum average subarray

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""

from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        if k == 1:
            return max(nums)
            
        current_sum = sum(nums[0:k])
        max_sum = current_sum
        
        for i in range(1, len(nums) - k + 1):
            current_sum -= nums[i-1]
            current_sum += nums[i+k-1]
            
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum / k
    

# Test 1:
nums = [1,12,-5,-6,50,3]
k = 4

solution = Solution()
result = solution.findMaxAverage(nums, k)
print(result)
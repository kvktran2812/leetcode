# Longest subarray of 1s after deleting one 0

"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""

from typing import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [-1]
        max_window = 0
        
        for i in range(n):
            if nums[i] == 0:
                arr.append(i)
        arr.append(n)

        m = len(arr)
        if m <= 3:
            return n - 1

        current_window = 0
        for i in range(1, m-1):
            current_window = arr[i+1] - arr[i-1] - 2
            # print(current_window)
            if current_window > max_window:
                max_window = current_window
                
        return max_window
    

# Test 1
nums = [1,1,0,1]

solution = Solution()
result = solution.longestSubarray(nums)
print(result)


# Test 2:
nums = [0,1,1,0,1]

solution = Solution()
result = solution.longestSubarray(nums)
print(result)


# Test 3:
nums = [0,1,1,0,1,1,1,1,0,1,1]

solution = Solution()
result = solution.longestSubarray(nums)
print(result)
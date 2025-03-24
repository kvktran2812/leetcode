# Max consecutive ones

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

from typing import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        h = 0
        max_window = 0
        n = len(nums)

        if k >= n:
            return n

        while j < n:
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0 and h < k:
                j += 1
                h += 1
            else:
                if nums[i] == 1:
                    i += 1
                else:
                    i += 1
                    h -= 1

            current_window = j - i

            if current_window > max_window:
                max_window = current_window
            
        return max_window
    

# Test 1:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

solution = Solution()
result = solution.longestOnes(nums, k)
print(result)


# Test 2:
nums = [0,0,1,1]
k = 1

solution = Solution()
result = solution.longestOnes(nums, k)
print(result)
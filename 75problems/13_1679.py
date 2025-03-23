# Max number of K-Sum pairs

"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import *

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n_dict = {}
        count = 0
        for i in nums:
            if i in n_dict:
                n_dict[i] += 1
            else:
                n_dict[i] = 1

        for i in n_dict:
            if i == k / 2:
                count += n_dict[i] // 2
            else:
                if k - i in n_dict:
                    t = min(n_dict[i], n_dict[k-i])
                    count += t
                    n_dict[i] -= t
                    n_dict[k-i] -= t
        return count
    

# Test 1:
nums = [1,2,3,4]
k = 5

solution = Solution()
result = solution.maxOperations(nums, k)
print(result)


# Test 2:
nums = [3,1,3,4,3]
k = 6

solution = Solution()
result = solution.maxOperations(nums, k)
print(result)
# Move Zeros problem

from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        if j == 0:
            return

        while i != j:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j -= 1
            else:
                i += 1
        return 
    

# Test 1:
nums = [0,1,0,3,12]
solution = Solution()
result = solution.moveZeroes(nums)
print(nums)

# Test 2:
nums = [0]
solution = Solution()
result = solution.moveZeroes(nums)
print(nums)
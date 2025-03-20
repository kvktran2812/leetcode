from typing import *
from math import *

# Can Place Flowers problem

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = 0
        right = 0

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if i > 0:
                left = flowerbed[i-1]
            if i < len(flowerbed) - 1:
                right = flowerbed[i+1]
            if left == 0 and right == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True
        
        return False

# Test 1    
flowerbed = [1,0,0,0,1]
n = 1

solution = Solution()
result = solution.canPlaceFlowers(flowerbed, n)
print(result)       # True
print(flowerbed)    # [1,0,1,0,1]


# Test 2
flowerbed = [1,0,0,0,1]
n = 2

solution = Solution()
result = solution.canPlaceFlowers(flowerbed, n)
print(result)       # False
print(flowerbed)    # [1,0,1,0,1]
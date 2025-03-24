# Find the Highest Altitude

"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.
"""

from typing import *

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prev = 0
        best = 0
        for i in range(len(gain)):
            # prev = new_gain
            new_gain = gain[i] + prev
            prev = new_gain
            # print(new_gain)
            if new_gain > best:
                best = new_gain
        return best
    

# Test 1:
gain = [-5,1,5,0,-7]

solution = Solution()
result = solution.largestAltitude(gain)
print(result)


# Test 2:
gain = [-4,-3,-2,-1,4,3,2]
solution = Solution()
result = solution.largestAltitude(gain)
print(result)
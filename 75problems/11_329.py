# Is Subsequence

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

from typing import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(t)):
            if s[0] == t[i]:
                if len(s) == 1:
                    return True
                else:
                    return True and self.isSubsequence(s[1:], t[i+1:])
        return False
    

# Test 1: 
s = "abc"
t = "ahbgdc"

solution = Solution()
result = solution.isSubsequence(s, t)
print(result)

# Test 2:
s = "axc"
t = "ahbgdc"

solution = Solution()
result = solution.isSubsequence(s, t)
print(result)
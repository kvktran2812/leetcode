from typing import *
from math import *

# Reverse Vowels of a String problem

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        pos = []
        str = []
        
        for i in range(len(s)):
            str.append(s[i])
            if s[i].lower() in vowels:
                pos.append(i)

        for i in range(len(pos) // 2):
            str[pos[i]], str[pos[-i-1]] = str[pos[-i-1]], str[pos[i]]
        return "".join(str)
    

# Test 1
s = "IceCreAm"

solution = Solution()
result = solution.reverseVowels(s)

print(result) # AceCreIm



# Test 2
s = "leetcode"

solution = Solution()
result = solution.reverseVowels(s)

print(result) # leotcede
from typing import *
from math import *

# Reverse words in string problem

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        reverse = []

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                word.append(s[i])
            if s[i] == " " or i == 0:
                if word != []:
                    if reverse != []:
                        reverse.append(" ")
                    for j in range(len(word) - 1, -1, -1):
                        reverse.append(word[j])
                word = []
        return "".join(reverse)
    

# Test 1
s = "the sky is blue"

solution = Solution()
result = solution.reverseWords(s)
print(result) # blue is sky the


# Test 2
s = "  hello     world  "

solution = Solution()
result = solution.reverseWords(s)
print(result) # world hello
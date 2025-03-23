# Maximum Number of Vowels in a Substring of Given Length

"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

from typing import *

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "u", "o", "i"]
        n = len(s)
        current_vowel = 0
        
        for i in range(k):
            if s[i] in vowels:
                current_vowel += 1
    
        max_vowel = current_vowel
        
        for i in range(1, n - k + 1):
            if s[i-1] in vowels:
                current_vowel -= 1
            if s[i+k-1] in vowels:
                current_vowel += 1
            if current_vowel > max_vowel:
                max_vowel = current_vowel
            if max_vowel == k:
                return max_vowel
        return max_vowel
    

# Test 1:
s = "abciiidef"
k = 3

solution = Solution()
result = solution.maxVowels(s, k)
print(result)


# Test 2:
s = "aeiou"
k = 2

solution = Solution()
result = solution.maxVowels(s, k)
print(result)


# Test 3:
s = "leetcode"
k = 3

solution = Solution()
result = solution.maxVowels(s, k)
print(result)
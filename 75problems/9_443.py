# String Compression problem

from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 1
        idx = 0
        c = chars[0]
        count = 1

        if len(chars) == 1:
            return 1
        
        while i < len(chars):
            if c != chars[i]:
                chars.insert(idx, c)
                i += 1
                idx += 1
                
                if count > 1:
                    for j in str(count):
                        chars.insert(idx, j)
                        idx += 1
                        i += 1
                c = chars[i]
                count = 1
            else:
                count += 1

            if i + 1 == len(chars):
                chars.insert(idx, c)
                i += 1
                idx += 1
                if count > 1:
                    for j in str(count):
                        chars.insert(idx, j)
                        idx += 1
                        i += 1
            i += 1

        for i in range(n):
            chars.pop()
        return len(chars)
    

# Test 1:
chars = ["a"]
solution = Solution()
result = solution.compress(chars)
print(result)
print(chars)

# Test 2:
chars = ["a", "b"]
solution = Solution()
result = solution.compress(chars)
print(result)
print(chars)

# Test 3:
chars = ["a", "b", "b", "b"]
solution = Solution()
result = solution.compress(chars)
print(result)
print(chars)
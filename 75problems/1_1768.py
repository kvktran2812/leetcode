# 1768. Merged String ALternately

class Solution: 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged_str = []

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged_str.append(word1[i])
            if i < len(word2):
                merged_str.append(word2[i])
            i += 1

        return "".join(merged_str)
    

solution = Solution()
print(solution.mergeAlternately("ab", "pqrs"))
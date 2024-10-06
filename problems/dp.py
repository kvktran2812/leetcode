from typing import List, Dict, Set
from structures.tree import TreeNode

def climbing(steps: int) -> int:
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    
    L = [-1] * (steps + 1)
    L[0] = 0
    L[1] = 1
    L[2] = 2

    for i in range(3, steps+1):
        L[i] = L[i-1] + L[i-2]
    return L[-1]

def fibonacci(n: int) -> int:
    if n == 0:
            return 0
    if n == 1:
        return 1
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    i = 2
    while (i <= n):
        fib[i] = fib[i-1] + fib[i-2]
        i += 1

    return fib[n]

def longest_common_subsequence(X: str, Y: str) -> int:
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[m - i] == Y[n - j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    return dp[m][n] 


def count_bits(n: int) -> List[int]:
    if n == 0:
        return [0]
    
    ans = [0] * (n + 1)
    ans[0] = 0
    ans[1] = 1
    
    for i in range(2, n + 1):
        if i % 2 == 0:
            ans[i] = ans[i // 2]
        if i % 2 == 1:
            ans[i] = ans[i // 2] + 1
    return ans

def possible_full_binary_trees(n : int) -> int:
    if n % 2 == 0:
        return []
    dp = {
        1: [TreeNode(0)]
    }

    def generate_tree(nodes: int):
        if nodes in dp:
            return dp[nodes]

        trees = []
        for i in range(1, nodes, 2):
            j = nodes - i - 1
            l_trees = generate_tree(i)
            r_trees = generate_tree(j)
            
            for left in l_trees:
                for right in r_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    trees.append(root)
        dp[nodes] = trees
        return trees
    return generate_tree(n)

def countVowelStrings(n: int) -> int:
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


def count_vowels_strings_dp(n: int) -> int:
    if n == 1:
        return 5

    dp = [[] for _ in range(n)]
    dp[0] = ['a', 'e', 'i', 'o', 'u']

    for i in range(1, n):
        for j in range(len(dp[i-1])):
            for k in range(5):
                if dp[0][k] < dp[i-1][j][-1]:
                    dp[i].append(dp[i-1][j] + dp[0][k])

    return dp, len(dp[-1])
from typing import List, Dict, Set

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
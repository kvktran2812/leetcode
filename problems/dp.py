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


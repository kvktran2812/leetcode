from typing import List, Dict, Set

def limbing(steps: int) -> int:
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
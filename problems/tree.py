from typing import List

"""
at index i
    left child node: 2*i + 1
    right child node: 2*i + 2 
"""

class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.left = left
        self.right = right
        self.val = val

def min_abs_diff(root: List[int]) -> int:
    """
    Function to calculate minimum absolute different between two nodes 

    :return: An interger indicates the absolute minimum value
    :rtype: int
    """
    abs_min = 0

    

    return -1
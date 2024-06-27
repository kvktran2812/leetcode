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
    abs_min = 999999
    size = len(root)
    next_node = [0]

    while next_node != []:
        node = next_node[0]
        left = node * 2 + 1
        right = node * 2 + 2

        if left < size:
            if root[left] != None:
                diff = abs(root[left] - root[node])
                if diff < abs_min:
                    abs_min = diff
                next_node.append(left)
        if right < size:
            if root[right] != None:
                diff = abs(root[right] - root[node])
                if diff < abs_min:
                    abs_min = diff
                next_node.append(right)
        next_node.pop(0)

    return abs_min
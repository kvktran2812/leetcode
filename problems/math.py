from typing import List, Dict, Set

def plusOne(digits: List[int]) -> List[int]:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Args:
        digits (List[int]): List of int representation of the number

    Returns:
        List[int]: Return the increment representation of the number
    """
    for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[i] += 1
                break
    return digits
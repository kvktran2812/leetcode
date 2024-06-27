import pytest
from problems import math

@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1, 0])
    ]
)
def test_plusOne(digits, expected):
    """
    Test module for plusOne function in problems.math

    Args:
        digits (List[int]): List of int represent the number
        expected (List[int]): List of int represent the increment of the number
    """
    outputs = math.plusOne(digits)
    assert outputs == expected
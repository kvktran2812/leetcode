import pytest
from problems import tree

@pytest.mark.parametrize(
        "root, expected", 
        [
            ([4,2,6,1,3], 1),
            ([1,0,48,None,None,12,49], 1)
        ]
)
def test_min_abs_diff(root, expected):
    outputs = tree.min_abs_diff(root)
    assert outputs == expected
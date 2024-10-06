import pytest
from problems import dp


@pytest.mark.parametrize(
        "steps, expected",
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8)
        ]
)
def test_climbing(steps, expected):
    outputs = dp.climbing(steps)
    assert outputs == expected



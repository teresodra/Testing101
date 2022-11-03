from compare_lists import compare_sum
import pytest


@pytest.mark.parametrize(
    ['list1', 'list2', 'boolean'],
    [
        [[0, 1, 3], [2, 2], True],
        [[0, 2, 1], [2, 2, 1], False]
    ]
)
def test_compare_sum(list1, list2, boolean):
    assert compare_sum(list1, list2) == boolean
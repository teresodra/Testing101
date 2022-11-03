from compare_lists.compare_sum import compare_sum
from compare_lists.operations.my_sum import my_sum
import pytest

@pytest.mark.parametrize(
    ['list1', 'list2', 'boolean'],
    [[[1, 2, 3], [2, 1, 1, 2], True],
    [[2,1,3], [3,4], False]]
)
def test_compare_sum(list1, list2, boolean):
    assert compare_sum(list1,list2) == boolean

def test_compare_sum_not_list():
    with pytest.raises(TypeError):
        compare_sum('a',[0,1])

def test_my_sum_complex():
    with pytest.raises(Exception):
        my_sum([1+1j])

def test_my_sum_complex2():
    with pytest.raises(TypeError):
        my_sum(['2',3])
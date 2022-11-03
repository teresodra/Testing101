from compare_lists.fibonacci.fibonacci import fibonacci
import pytest

@pytest.mark.parametrize(['input', 'output'],
[[4,5],[5,8],[6,13]])
def test_fibonacci(input,output):
    assert fibonacci(input)==output
def test_fibonacci_with_neg_numbers():
    with pytest.raises(Exception):
        fibonacci(-1)
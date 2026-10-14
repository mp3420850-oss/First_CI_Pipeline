
from importlib import import_module
import pytest

find_max_min = import_module("25_max_min_list").find_max_min


def test_positive_numbers():
    assert find_max_min([3, 1, 9, 4]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -10]) == (-2, -10)


def test_mixed_numbers():
    assert find_max_min([-3, 0, 8, -1]) == (8, -3)


def test_single_number():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_empty_list_raises_error():
    with pytest.raises(ValueError):
        find_max_min([])

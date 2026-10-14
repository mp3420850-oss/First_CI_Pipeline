
from importlib import import_module

rotate_list = import_module("27_rotate_list").rotate_list


def test_rotate_right_once():
    assert rotate_list([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]


def test_rotate_right_twice():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_by_list_length():
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]


def test_rotate_more_than_length():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


def test_negative_rotation():
    assert rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

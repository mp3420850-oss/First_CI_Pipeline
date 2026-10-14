
from importlib import import_module

sum_of_list = import_module("26_sum_of_list").sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_list([-2, 5, 3]) == 6


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_number():
    assert sum_of_list([7]) == 7


def test_zeros():
    assert sum_of_list([0, 0, 0]) == 0


from importlib import import_module

set_intersection = import_module("28_set_intersection").set_intersection


def test_common_elements():
    assert set(set_intersection([1, 2, 3], [2, 3, 4])) == {2, 3}


def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


def test_both_lists_empty():
    assert set_intersection([], []) == []


def test_duplicate_elements():
    assert set(set_intersection([1, 1, 2, 2], [2, 2, 3])) == {2}


def test_negative_numbers():
    assert set(set_intersection([-1, -2, 3], [-2, 3, 4])) == {-2, 3}


def test_identical_lists():
    assert set(set_intersection([1, 2, 3], [1, 2, 3])) == {1, 2, 3}

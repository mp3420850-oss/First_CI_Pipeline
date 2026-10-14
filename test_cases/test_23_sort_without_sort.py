
from importlib import import_module

bubble_sort = import_module("23_sort_without_sort").bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_duplicates():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_empty_list():
    assert bubble_sort([]) == []


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]

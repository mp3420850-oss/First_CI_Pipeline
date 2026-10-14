
from importlib import import_module

is_anagram = import_module("22_anagram_strings").is_anagram


def test_anagrams():
    assert is_anagram("listen", "silent") is True


def test_not_anagrams():
    assert is_anagram("hello", "world") is False


def test_ignores_uppercase():
    assert is_anagram("Listen", "Silent") is True


def test_ignores_spaces():
    assert is_anagram("dormitory", "dirty room") is True


def test_empty_strings():
    assert is_anagram("", "") is True

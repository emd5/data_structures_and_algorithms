from .insertion_sort import insertion_sort
from random import shuffle
import pytest


def test_shuffled_list_gets_sorted():
    expected = [num in num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    insertion_sort(sorted)
    now_sorted = insertion_sort(unsorted)
    assert expected == now_sorted


def test_sorts_already_sorted():
    expected = [num in num in range(20)]
    now_sorted = insertion_sort(expected)
    assert expected == now_sorted


def test_sorts_list_of_duplicates():
    unsorted = [4, 4, 5, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = insertion_sort(unsorted)
    assert expected == now_sorted


def test_sort_validates_expected_input():
    with pytest.raises(TypeError):
        insertion_sort('hello world')




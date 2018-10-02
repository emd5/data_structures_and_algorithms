from .mergesort import mergesort
import pytest


def test_merge_sort_method_exist():
    """Test merge sort method exist"""
    assert mergesort


def test_merge_sort_is_successful():
    """Test merge sort is successful"""
    actual = [34, 19, 42, -9, 2018, 0, 2005, 77, 2099]
    expected = [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]
    assert mergesort(actual) == expected


def test_merge_sort_with_characters():
    """Test merge sort with letters"""
    assert mergesort(['c', 'b', 'a']) == ['a', 'b', 'c']


def test_merge_sort_with_one_number():
    """Test with one number"""
    assert mergesort([1]) == [1]


def test_with_empty_list():
    """Test merge sort method with an empty list raises assertion error"""
    with pytest.raises(AssertionError):
        assert mergesort([])




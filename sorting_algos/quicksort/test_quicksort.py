from .quicksort import quicksort
import pytest


def test_quick_sort_method_exist():
    """Test method exist from other file"""
    assert quicksort


def test_quick_sort_with_numbers_is_successful():
    """Test quick sort method returns expected array"""
    actual = [4, 3, 2, 1]
    expected = [1, 2, 3, 4]
    assert quicksort(actual) == expected


def test_quick_sort_raised_assertion_error():
    """Test quick sort method when passed in empty array"""
    with pytest.raises(AssertionError):
        assert quicksort([])


def test_quick_sort_with_letters_is_successful():
    """Test quick sort with an array of letter"""
    actual = ['e', 'c', 'b', 'a', 'd']
    expected = ['a', 'b', 'c', 'd', 'e']
    assert quicksort(actual) == expected


def test_quick_sort_with_one_value():
    """Test with a one value in the array"""
    assert quicksort([1]) == [1]






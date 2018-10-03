from .radixsort import radix_sort
import pytest


def test_radix_sort_is_successful():
    """Test an array with values returns successful """
    assert radix_sort([400, 500, 213, 456]) == [213, 400, 456, 500]


def test_reverse_array_is_successful():
    """Test array with zeros, returns true"""
    assert radix_sort([10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000]


def test_with_zero_value_raises_error():
    """Test an array with zero value should raise exception"""
    with pytest.raises(AssertionError):
        expected = radix_sort([10000, 1000, 100, 10, 0])
        assert expected == [0, 10, 100, 1000, 10000]


def test_empty_list_raises_assertion_error():
    """Test an empty list raises exception error"""
    with pytest.raises(AssertionError):
        assert radix_sort([])


def test_single_index_array():
    """Test letters in array raise assertion error"""
    with pytest.raises(TypeError):
        assert radix_sort(['c', 'b', '1']) == ['a', 'b', 'c']

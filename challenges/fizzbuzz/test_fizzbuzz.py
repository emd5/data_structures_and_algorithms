from .fizzbuzz import fizzbuzz
import pytest


# All the fizzbuzz tests
def test_fizzbuzz_exist():
    """Test file and method exist """
    assert fizzbuzz


def test_fizzbuzz_with_3():
    """Test 9/3  is successful, remainder is 0 """
    assert fizzbuzz(9) == 'fizz'


def test_fizzbuzz_with_5():
    """Test 10/5 is successful, remainder is 0 """
    assert fizzbuzz(10) == 'buzz'


def test_fizzbuzz_is_both_successful():
    """Test 15/5 & 15/3 returns fizzbuzz, both remainders is 0"""
    assert fizzbuzz(15) == 'fizzbuzz'


def test_fizzbuzz_returns_input_value():
    """Test value that successfully returns its self"""
    assert fizzbuzz(7) == 7


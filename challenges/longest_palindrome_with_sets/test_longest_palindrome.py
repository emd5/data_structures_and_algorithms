from .longest_palindrome import longest_palindrome
import pytest


def test_method_exists():
    """Test method exists from another file"""
    assert longest_palindrome


def test_has_longest_palindrome():
    """Test longest palindrome returns 6"""
    assert longest_palindrome('cattac') == 6


def test_does_not_have_longest_palindrome():
    """Test when the word is not a palindrome, returns 1"""
    assert longest_palindrome('tac') == 1


def test_palindrome_has_numbers_as_string():
    """Test input with numbers as a string"""
    assert longest_palindrome('98765432123456789') == 17


def test_palindrome_is_a_value():
    """An argument that is not a string, returns a TypeError"""
    with pytest.raises(TypeError):
        assert longest_palindrome(23423423)

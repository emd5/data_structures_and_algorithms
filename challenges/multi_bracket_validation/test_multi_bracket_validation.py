from .multi_bracket_validation import multi_bracket_validation
import pytest


def test_multi_bracket_validation_exist():
    """Test method exist."""
    assert multi_bracket_validation


def test_balanced_nested_bracket_validation_is_true():
    """Test the stack is empty as a true result of a balanced nested brackets."""
    assert multi_bracket_validation('{([])}') is True


def test_balanced_with_words_is_true():
    """Test the stack is empty as a true result of a balanced nested brackets."""
    assert multi_bracket_validation('{}{Code}[Fellows](())') is True


def test_balanced_grouped_bracket_validation():
    """Test the input string is in the format of {}[](). """
    assert multi_bracket_validation('{}[]()') is True


def test_unbalanced_bracket():
    """Test the input string is unbalanced."""
    assert multi_bracket_validation('([]]]') is False


def test_unbalanced_bracket_2():
    """Test the input string is unbalanced with '(]('."""
    assert multi_bracket_validation('(](') is False


def test_unbalanced_overlapping_bracket():
    """Test an error where overlapping brackets fails."""
    assert multi_bracket_validation('([)]') is False


def test_unbalanced_with_one_character():
    """Test when there is one character"""
    assert multi_bracket_validation('[') is False

from .roman import Roman
import pytest


def test_method_exist():
    """Test the method in the Roman class can be used or exist"""
    assert Roman.int_to_roman


def test_integer_4_is_successful():
    """Test the integer 4 if passes"""
    roman = Roman()
    assert roman.int_to_roman(4) == 'IV'


def test_integer_9_is_successful():
    """Test the integer 9 passes successfully with IX."""
    roman = Roman()
    assert roman.int_to_roman(9) == 'IX'


def test_integer_58_is_successful():
    """Test the integer 58 passes successfully with LVIII."""
    roman = Roman()
    assert roman.int_to_roman(58) == 'LVIII'


def test_integer_3999_is_successful():
    """Test the integer 3999 passes successfully with MMMCMXCIX."""
    roman = Roman()
    assert roman.int_to_roman(3999) == 'MMMCMXCIX'


def test_integer_4000_is_fails():
    """Test the integer 4000 fails."""
    with pytest.raises(IndexError):
        roman = Roman()
        assert roman.int_to_roman(4000)







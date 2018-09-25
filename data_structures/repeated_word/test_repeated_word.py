from .repeated_word import repeated_word
import pytest


book1 = "Once upon a time, there was a brave princess who..."

book2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of " \
        "foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, " \
        "it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything " \
        "before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other " \
        "way – in short, the period was so far like the present period, that some of its noisiest authorities " \
        "insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

book3 = "A dog"


def test_repeated_word_exist():
    """Test function exist"""
    assert repeated_word


def test_repeated_word_has_repeats_book_1():
    """Test for repeated word in book 1"""
    assert repeated_word(book1) == 'a'


def test_repeated_word_has_repeats_book_2():
    """Test for repeated word in book 2"""
    assert repeated_word(book1) == 'a'


def test_for_empty_book():
    """Test empty book raises index error"""
    with pytest.raises(IndexError):
        assert repeated_word('')


def test_repeated_word_no_repeats():
    """Test no repeats returns No repeated words"""
    assert repeated_word(book3) == "No repeated words"




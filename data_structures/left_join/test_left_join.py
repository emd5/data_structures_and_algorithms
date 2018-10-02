from .left_join import left_join
from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_hash_table():
    empty_ht = HashTable()
    return empty_ht


@pytest.fixture
def setup1():
    """Setup hash table 1"""
    ht1 = HashTable()
    ht1.set('Apple', 'Jack')
    ht1.set('Pinky', 'Pie')
    ht1.set('Flutter', 'Shy')
    return ht1


@pytest.fixture
def setup2():
    """Setup hash table 2"""
    ht2 = HashTable()
    ht2.set('Apple', 'Dash')
    ht2.set('Flutter', 'Sparkle')
    ht2.set('Pinky', 'Pony')
    return ht2


def test_left_join_method_exist():
    assert left_join


def test_empty_hash_table_exist():
    assert empty_hash_table


def test_left_join_method_is_successful(setup1, setup2):
    """Test hash table 2 left joins with hash table 1."""
    assert left_join(setup1, setup2) == [['Apple', 'Jack']]

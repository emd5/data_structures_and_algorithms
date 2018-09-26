from .hash_table import HashTable
import pytest


@pytest.fixture
def set_up_hash_table():
    hash_table = HashTable()
    h = hash_table.table_size
    return h


def test_size_hash_table(set_up_hash_table):
    assert set_up_hash_table == 8192


def test_hash_table_class_exist():
    assert HashTable


def test_hash_table_is_set_successful(set_up_hash_table):
    assert set_up_hash_table.set('A', 1) is True


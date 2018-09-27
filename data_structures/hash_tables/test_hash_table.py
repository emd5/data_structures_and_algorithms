from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_hash_table():
    """Setup empty hash table"""
    hash_table = HashTable()
    return hash_table


@pytest.fixture
def setup_hash_table():
    """Setup hash table with key and value"""
    hash_table = HashTable()
    hash_table.set('Apple', 'Jack')
    hash_table.set('Joe', 'Schmoe')
    return hash_table


def test_hash_table_class_exist():
    """Test HashTable class exist"""
    assert HashTable


def test_size_hash_table():
    """Test length of hash table is 8192"""
    hash_table = HashTable()
    assert hash_table.table_size == 8192


def test_hash_table_is_set_successful():
    """Test add key and value to hash table is true"""
    hash_table = HashTable()
    assert hash_table.set('Apple', 'Jack') is True


def test_hash_table_add_same_existing_key():
    """Test add another key and value to hash table is true"""
    hash_table = HashTable()
    assert hash_table.set('Apple', 'Jack') is True
    assert hash_table.set('Apple', 'Jack') is True


def test_get_key_exists(setup_hash_table):
    """Test for key in hash table exist"""
    assert setup_hash_table.get('Apple') == 'Jack'




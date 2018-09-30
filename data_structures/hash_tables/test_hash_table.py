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
    hash_table.set('Flutter', 'Shy')
    hash_table.set('Rarity', 'Cutie')
    return hash_table


def test_hash_table_class_exist():
    """Test HashTable class exist"""
    assert HashTable


def test_size_hash_table():
    """Test length of hash table is 8192"""
    hash_table = HashTable()
    assert hash_table.table_size == 8192


def test_hash_table_is_set_successful(setup_hash_table):
    """Test add key and value to hash table is true"""
    assert setup_hash_table.set('Rainbow', 'Dash') is True


def test_add_existing_key_will_override_new_value(setup_hash_table):
    """Test add existing key that will append key and value to end of list """
    assert setup_hash_table.set('Apple', 'John') is True


def test_get_key_exists(setup_hash_table):
    """Test for key in hash table exist"""
    assert setup_hash_table.get('Apple') == 'Jack'


def test_get_key_does_not_exist(setup_hash_table):
    """Test for key in hash table does not exist"""
    assert setup_hash_table.get('John') is None


def test_remove_key_from_empty_hash_table(empty_hash_table):
    """Test remove a nonexistent key from empty hash table returns False"""
    assert empty_hash_table.remove('Test') is False


def test_remove_key_that_does_not_exist(setup_hash_table):
    """Test remove a key from filled hash table returns false"""
    assert setup_hash_table.remove('Test_fake_key') is False


def test_remove_key_that_exist(setup_hash_table):
    """Test remove a existing key from hash table is True """
    assert setup_hash_table.remove('Apple') is True

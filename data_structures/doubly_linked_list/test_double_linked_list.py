import pytest
from .double_linked_list import DoublyLinkedList


@pytest.fixture
def empty_dll_setup():
    """Set up an empty double linked list"""
    empty_dll = DoublyLinkedList()
    return empty_dll


@pytest.fixture
def dll_setup():
    """Set up a doubly linked list with values"""
    dll = DoublyLinkedList([3, 2, 16, 34, 21])
    return dll


def test_doubly_linked_list_class_exist():
    """Test doubly linked list module exist"""
    assert DoublyLinkedList


def test_setup_empty_dll(empty_dll_setup):
    """Test pytest fixture for empty_dll_setup"""
    assert isinstance(empty_dll_setup, DoublyLinkedList)


def test_setup_dll(dll_setup):
    """Test pytest fixture for dll_setup"""
    assert isinstance(dll_setup, DoublyLinkedList)


def test_append_method_exist():
    """Test append method exist from the DDL class"""
    assert DoublyLinkedList.insert


def test_remove_method_exist():
    """Test remove method exist from the DDL class"""
    assert DoublyLinkedList.remove


def test_find_method_exist():
    """Test find method exist from the DDL class"""
    assert DoublyLinkedList.find


def test_insert_at_head_of_empty_dll(empty_dll_setup):
    assert len(empty_dll_setup) == 0
    empty_dll_setup.insert(4)
    assert len(empty_dll_setup) == 1
    assert empty_dll_setup.head.value == 4


def test_insert_at_head_of_dll(dll_setup):
    assert len(dll_setup) == 5
    dll_setup.insert(24)
    assert len(dll_setup) == 6
    assert dll_setup.head.value == 24


def test_append_in_middle_of_dll(dll_setup):
    assert len(dll_setup) == 5


def test_append_at_end_of_dll():
    pass

import pytest

@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    return ll

def test_linked_lists_exist():
    assert LinkedList

def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

def test_default_property_head(empty_list):
    assert empty_list.head is None

def test_default_property_length(empty_list):
    assert empty_list._length == 0

def test_insertion_successful(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25

def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1

def test_includes_returns_true_if_exists(small_list):
    actual = small_list.includes(4)
    assert actual is True



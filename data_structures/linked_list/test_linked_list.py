from .linked_list import LinkedList
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
    return ll # ll = [5,4,3,2,1]


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


def test_append_to_list(small_list):
    assert small_list.append(90) is True


def test_insert_before_list(small_list):
    small_list.insert_before(3, 25)
    assert small_list.includes(25) is True


def test_insert_after_list(small_list):
    small_list.insert_after(4, 26)
    assert small_list.includes(26) is True


def test_insert_after_at_end_of_list(small_list):
    small_list.insert_after(5, 27)
    assert small_list.includes(27) is True


def test_kth_from_the_end_with_value(small_list):
    assert small_list.kth_from_the_end(3) == 4

def test_kth_from_the_end_no_value_in_list(small_list):
    with pytest.raises(AttributeError):
        small_list.kth_from_the_end(50)


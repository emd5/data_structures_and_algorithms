from .linked_list import LinkedList
from .ll_merge import merge_list
import pytest


@pytest.fixture
def empty_list():
    """Set up an empty list. """
    return LinkedList()


@pytest.fixture
def small_list():
    """Set up a linked list with values.

    :return
        a non-empty list
    """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    return ll


@pytest.fixture
def linked_list_1():
    """Set up a linked list with values for the merge list.

    :return
        a non-empty list
    """
    ll_1 = LinkedList()
    ll_1.insert(1)
    ll_1.insert(3)
    ll_1.insert(5)
    ll_1.insert(7)
    ll_1.insert(9)
    return ll_1


@pytest.fixture
def linked_list_2():
    """Set up a second linked list with values for the merge list.

    :return
        a non-empty list
    """
    ll_2 = LinkedList()
    ll_2.insert(2)
    ll_2.insert(4)
    ll_2.insert(6)
    ll_2.insert(8)
    ll_2.insert(10)
    return ll_2


def test_linked_lists_exist():
    """Tests if linked list exist. """
    assert LinkedList


def test_create_instance_of_list():
    """Tests an instance of a list. """
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_create_instance_of_ll_1():
    """Tests an instance of a linked list 1. """
    ll_1 = LinkedList()
    assert isinstance(ll_1, LinkedList)


def test_create_instance_of_ll_2():
    """Tests an instance of a linked list 2. """
    ll_2 = LinkedList()
    assert isinstance(ll_2, LinkedList)


def test_default_property_head(empty_list):
    """Tests empty list head is none. """
    assert empty_list.head is None


def test_default_property_length(empty_list):
    """Tests the empty list's length is equal to 0. """
    assert empty_list._length == 0


def test_insertion_successful(empty_list):
    """Test insertion on empty list where value is found. """
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    """Tests empty list's length after insertion is equal to one. """
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    """Test to confirm the value is in the small list. """
    actual = small_list.includes(4)
    assert actual is True


def test_append_to_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.append(4)
    assert small_list.includes(4) is True


def test_insert_before_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.insert_before(3, 25)
    assert small_list.includes(25) is True


def test_insert_after_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.insert_after(4, 26)
    assert small_list.includes(26) is True


def test_insert_after_at_end_of_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.insert_after(5, 27)
    assert small_list.includes(27) is True


def test_kth_from_the_end_with_value(small_list):
    """Test to the last value in the small list is equal to the value """
    assert small_list.kth_from_the_end(3) == 4


def test_kth_from_the_end_no_value_in_list(small_list):
    """Test to add a value to the small list and value is found. """
    with pytest.raises(AttributeError):
        small_list.kth_from_the_end(50)


def test_merge_list_exist(linked_list_1, linked_list_2):
    """Test merge functions to. """
    assert merge_list(linked_list_1, linked_list_2) is True




from .linked_list import LinkedList
from .ll_merge import get_merge_list
import pytest


@pytest.fixture
def empty_list():
    """Set up an empty list. """
    return LinkedList([])


@pytest.fixture
def small_list():
    """Set up a linked list with values.

    :return
        a non-empty list
    """
    ll = LinkedList([1, 2, 3, 4, 5])
    return ll


@pytest.fixture
def linked_list_1():
    """Set up a linked list with values for the merge list.

    :return
        a non-empty list
    """
    ll_1 = LinkedList([1, 3, 5, 7, 9])
    return ll_1


@pytest.fixture
def linked_list_2():
    """Set up a second linked list with values for the merge list.
    :return
        a non-empty list
    """
    ll_2 = LinkedList([2, 4, 6, 8, 10])
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


def test_head_of_small_list_on_insertion(small_list):
    small_list.insert(20)
    assert small_list.head.val == 20


def test_includes_returns_true_if_exists(small_list):
    """Test to confirm the value is in the small list. """
    expected = small_list.includes(4)
    assert expected is True


def test_includes_returns_false_if_not_exists(small_list):
    """Test to confirm the value is in the small list. """
    expected = small_list.includes(99)
    assert expected is False


def test_append_to_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.append(4)
    assert small_list.includes(4) is True


def test_insert_before_list_is_valid(small_list):
    """Test to add a value before the value to the small list. """
    small_list.insert_before(3, 20)
    current = small_list.head
    while current._next.val is not 3:
        current = current._next

    assert current.val == 20
    assert current._next.val == 3


def test_insert_before_head_is_valid(small_list):
    """Test insert at head. """
    small_list.insert_before(5, 99)
    assert small_list.head.val == 99
    assert small_list.head._next.val == 5


def test_insert_after_at_head(small_list):
    """Test add value after the head of the list. """
    small_list.insert_after(5, 26)
    current = small_list.head
    assert current.val == 5
    assert current._next.val == 26


def test_insert_after_at_middle(small_list):
    """Test insert after when add new value in the middle. """
    small_list.insert_after(3, 99)
    current = small_list.head
    while current.val is not 3:
        current = current._next

    assert current.val == 3
    assert current._next.val == 99
    assert current._next._next.val == 2


def test_insert_after_at_end_of_list(small_list):
    """Test to add a value to the small list and value is found. """
    small_list.insert_after(1, 99)
    current = small_list.head
    while current.val is not 1:
        current = current._next

    assert current.val == 1
    assert current._next.val == 99


def test_kth_from_the_end_with_value_in_list(small_list):
    """Test the value if it is in the list """
    assert small_list.kth_from_the_end(3) == 4


def test_kth_from_the_end_no_value_in_list(small_list):
    """Test to add a value to the small list and value is found. """
    actual = 'Your value is greater than length of list'
    assert small_list.kth_from_the_end(99) == actual


def test_merge_list_when_ll1_is_shorter():
    """Test when ll1 is shorter than ll2. """
    ll_1 = LinkedList([1, 3, 5])
    ll_2 = LinkedList([2, 4, 6, 8, 10])
    assert get_merge_list(ll_1, ll_2) == 5
    # assert get_merge_list(ll_1, ll_2)._next == 10


# def test_merge_list_when_ll2_is_shorter():
#     """Test when ll1 is shorter than ll2. """
#     ll_2 = LinkedList([1, 3, 5])
#     ll_1 = LinkedList([2, 4, 6, 8, 10])
#     assert get_merge_list(ll_1, ll_2).val == 5
#     assert get_merge_list(ll_1, ll_2)._next.val == 10




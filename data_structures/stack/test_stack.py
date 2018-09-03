from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    """Set up an empty stack."""
    return Stack()


@pytest.fixture
def small_stack():
    """Set up a stack with some values. """
    stack = Stack([2, 40, 32, 14])
    return stack


def test_stack_exist():
    """Test if the stack class exist. """
    assert Stack


def test_default_property_head(empty_stack):
    """Test empty stack is none. """
    assert empty_stack.top is None


def test_default_property_length(empty_stack):
    """Test empty stack's length is equal to 0. """
    assert empty_stack._length == 0


def test_push_to_empty_stack_is_successful(empty_stack):
    """Test push to an empty stack. """
    assert empty_stack.top is None
    empty_stack.push(20)
    assert empty_stack.top.val == 20


def test_push_to_small_stack_is_successful(small_stack):
    """Test add to existing stack, passes when stack length increment by 1. """
    assert len(small_stack) == 4
    small_stack.push(78)
    assert len(small_stack) == 5


def test_remove_from_empty_stack(empty_stack):
    """Test remove from empty stack. """
    assert empty_stack.pop()


def test_peek_empty_stack(empty_stack):
    """Test peek from empty stack is None. """
    assert empty_stack.peek() is None


def test_peek_small_stack(small_stack):
    """Test peek from small stack equals to top. """
    assert small_stack.peek() == small_stack.top

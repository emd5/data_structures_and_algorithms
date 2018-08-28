from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    """Set up an empty stack."""
    return Stack()


@pytest.fixture
def small_stack():
    """Set up a stack with some values. """
    small_stack = Stack()
    small_stack.push(2)
    small_stack.push(40)
    small_stack.push(32)
    small_stack.push(14)
    return small_stack


def test_stack_exist():
    """Test if the stack class exist. """
    assert Stack


def test_default_property_head(empty_stack):
    """Test empty stack is none. """
    assert empty_stack.top is None


def test_default_property_length(empty_stack):
    """Test empty stack's length is equal to 0. """
    assert empty_stack._length == 0


def test_push_is_successful(empty_stack):
    """Test push to an empty stack. """
    assert empty_stack.top is None
    empty_stack.push(20)
    assert empty_stack.top.val == 20



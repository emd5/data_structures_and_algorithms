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

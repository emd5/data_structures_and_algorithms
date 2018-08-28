from .data_structures.stack import Stack
from .data_structures.queue import Queue
import pytest


@pytest.fixture
def empty_stack():
    """Set up an empty stack."""
    return Stack()


@pytest.fixture
def small_stack():
    """Set up a stack with some values. """
    small_stack = Stack()
    small_stack.push(1)
    small_stack.push(2)
    small_stack.push(3)
    small_stack.push(4)
    return small_stack











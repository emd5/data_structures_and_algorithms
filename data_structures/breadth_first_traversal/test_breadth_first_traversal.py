from .bst import BinaryTree
from .breadth_first_traversal import breadth_first_traversal
import pytest


@pytest.fixture
def small_binary_tree():
    """Test set up with binary tree instantiation. """
    bt = BinaryTree([30, 20, 10, 5, 50])
    return bt


def test_empty_binary_tree():
    """Test to instantiate a binary tree object. """
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree) is True


def test_breadth_first_traversal_exists():
    """Test the method  exists. """
    assert breadth_first_traversal


def test_breadth_first_traversal_with_bt():
    """Test method with an argument with a Binary tree. """
    bt = BinaryTree([30, 20, 10, 5, 50])
    breadth_first_traversal(bt.root) is True


def test_breath_first_traversal():
    """Test method """




















from .bst import BinaryTree
from .breadth_first_traversal import breadth_first_traversal
import pytest


def test_empty_binary_tree():
    """Test to instantiate a binary tree object. """
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree) is True


def test_breadth_first_traversal_exists():
    """Test the method  exists. """
    assert breadth_first_traversal


def test_breadth_first_traversal_with_bt():
    """Test method with an argument with a Binary tree. """
    bt = BinaryTree([50, 75, 100, 60, 25, 30, 10])
    expected = breadth_first_traversal(bt.root)
    actual = [50, 25, 75, 10, 30, 60, 100]
    assert expected == actual


def test_breath_first_traversal_with_duplicate_values():
    """Test method with duplicate values """
    with pytest.raises(ValueError):
        bt = BinaryTree([50, 75, 100, 60, 25, 50, 10])
        breadth_first_traversal(bt)




















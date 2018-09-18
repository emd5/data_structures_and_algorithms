from .bst import BinaryTree
from .breadth_first_traversal import breadth_first_traversal
import pytest


@pytest.fixture
def empty_tree():
    """Set up an empty tree"""
    empty_bt = BinaryTree([])
    return empty_bt


@pytest.fixture
def small_tree():
    """Set up a small binary tree."""
    small_bt = BinaryTree([50, 75, 100, 60, 25, 30, 10])
    return small_bt


def test_empty_binary_tree():
    """Test to instantiate a binary tree object."""
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree) is True


# def test_breadth_first_traversal_exists():
#     """Test the method exists."""
#     assert breadth_first_traversal


def test_breadth_first_traversal_with_bt(small_tree):
    """Test method with an argument with a Binary tree. """
    expected = breadth_first_traversal(small_tree)
    actual = [50, 25, 75, 10, 30, 60, 100]
    assert expected == actual


# def test_breath_first_traversal_with_duplicate_values(small_tree):
#     """Test method with duplicate values """
#     with pytest.raises(ValueError):
#         # bt = BinaryTree([50, 75, 100, 60, 25, 50, 10])
#         breadth_first_traversal(small_tree)
#
#
# def test_bfs_with_an_empty_list(empty_tree):
#     """Test an empty tree to return an assertion error"""
#     with pytest.raises(AssertionError):
#         breadth_first_traversal(empty_tree)



















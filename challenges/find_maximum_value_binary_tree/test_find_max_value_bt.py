from .bst import BinaryTree

from .find_max_value_bt import find_max_value_in_bt
import pytest


def test_empty_binary_tree():
    """Test to instantiate a binary tree object. """
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree) is True


def test_find_max_value_with_bt_exists():
    """Test the method exists. """
    assert find_max_value_in_bt


def test_find_max_value_with_empty_list():
    with pytest.raises(IndexError):
        bt = BinaryTree([50, 25, 35, 40, 3, 20, 100])
        find_max_value_in_bt(bt)

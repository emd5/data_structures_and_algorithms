from .tree_intersection import tree_intersection
from .bst import BinaryTree
import pytest


@pytest.fixture
def bst_1():
    """Set up binary tree 1."""
    bt1 = BinaryTree([20, 30, 12, 19, 20, 14, 40, 50, 22, 33])
    return bt1


@pytest.fixture
def bst_2():
    """Set up binary tree  2."""
    bt2 = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    return bt2


def test_tree_intersection_function_exist():
    """Test the function exist"""
    assert tree_intersection


def test_tree_intersection_has_output():
    assert tree_intersection(bst_1, bst_2) == [20, 30, 12, 19, 20, 14, 40, 50, 22, 33, 20, 18, 12, 19, 11, 14, 40, 31, 22, 33]


def test_tree_intersection_failed():
    pass


def test_tree_intersection_found_all():
    pass


def test_tree_intersection_found_one_output():
    pass

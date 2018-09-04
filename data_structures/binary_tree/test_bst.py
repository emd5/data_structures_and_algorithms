from .bst import BinaryTree, Node

import pytest


@pytest.fixture
def empty_tree():
    """Instantiate a empty tree"""
    no_tree = BinaryTree([])
    return no_tree


@pytest.fixture
def small_tree():
    """Create a small binary tree from a list"""
    small_tree = BinaryTree([5,3,1,2,8])
    return small_tree


def test_node_class():
    test_node = Node(1)
    assert test_node.val == 1


def test_binary_tree_class_exists():
    """Test binary tree class exist. """
    assert BinaryTree


def test_insert_empty_tree(empty_tree):
    """Test insert at the root with an empty list. """
    assert empty_tree.root is None
    empty_tree.insert(5)
    assert empty_tree.root.val == 5


def test_instance_of_small_tree():
    small_tree = BinaryTree([5, 3, 8, 2, 4, 6, 10])
    assert isinstance(small_tree, BinaryTree)


def test_in_order_method_is_successful(small_tree):
    """Test the order of each node to be """
    expected = small_tree.in_order()
    actual = BinaryTree([5, 3, 8, 2, 4, 6, 10])
    assert expected == actual


# def test_in_order_small_tree(small_tree):
#     """Test insert a value to a tree with Nodes. """
#     pass



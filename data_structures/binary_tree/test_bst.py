from .bst import BinaryTree
import pytest


def test_empty_bt():
    """Test an instance of an empty binary tree. """
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree)
    assert bt.root is None


def test_insert_into_empty_bt():
    """Test insert one node to a tree. """
    bt = BinaryTree()
    assert bt.root is None
    bt.insert(25)
    assert bt.root.value == 25


def test_iterable_creates_bt():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    assert bt.root.value == 20
    assert bt.root.left.value == 18
    assert bt.root.right.value == 40


def test_inorder_traversal():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    bt.in_order(generate_list)
    assert expected == actual


def test_preorder_traversal():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    bt.in_order(generate_list)
    assert expected == actual


def test_postorder_traversal():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    bt.in_order(generate_list)
    assert expected == actual



def test_insert_value_that_already_exists():
    bt = BinaryTree([25])
    with pytest.raises(ValueError):
        bt.insert(25)



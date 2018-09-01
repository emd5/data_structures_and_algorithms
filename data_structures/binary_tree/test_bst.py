from .bst import BinaryTree
import pytest


def test_binary_tree_exists():
    assert BinaryTree


def test_insert_empty_tree():
    tree = BinaryTree()
    assert tree.insert(34)




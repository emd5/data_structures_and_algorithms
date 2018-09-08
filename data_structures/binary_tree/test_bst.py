from .bst import BinaryTree
import pytest

@pytest.fixture
def empty_tree():
    """Set up an empty tree."""
    no_tree = BinaryTree([])
    return no_tree


@pytest.fixture
def small_tree():
    """Set up a small binary tree."""
    small_bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    return small_bt


def test_iterable_creates_bt(small_tree):
    """Test iterable works when creating a small tree."""
    assert small_tree.root.value == 20
    assert small_tree.root.left.value == 18
    assert small_tree.root.right.value == 40


def test_empty_bt(empty_tree):
    """Test an instance of an empty binary tree."""
    assert isinstance(empty_tree, BinaryTree)
    assert empty_tree.root is None


def test_insert_into_empty_bt(empty_tree):
    """Test insert one node to a tree. """
    assert empty_tree.root is None
    empty_tree.insert(25)
    assert empty_tree.root.value == 25


def test_insert_a_duplicate_value(small_tree):
    """Test insert an existing value in the binary tree,
    returns value error. """
    with pytest.raises(ValueError):
        small_tree.insert(14)


def test_in_order_traversal(small_tree):
    """Test all values are in ascending order."""
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    small_tree.in_order(generate_list)
    assert expected == actual


def test_pre_order_traversal(small_tree):
    """Test all values are in pre-order traversal."""
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    small_tree.in_order(generate_list)
    assert expected == actual


def test_post_order_traversal(small_tree):
    """Test all values are in post- order traversal."""
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)

    small_tree.in_order(generate_list)
    assert expected == actual




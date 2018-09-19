import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    """Set up an empty graph"""
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    """Set up a graph for traversal."""
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'D': 10},
        'B': {'A': 10, 'C': 10, 'D': 10},
        'C': {'B': 10, 'G': 10},
        'D': {'A': 10, 'B': 10, 'E': 10, 'H': 10, 'F': 10},
        'E': {'D': 10},
        'F': {'D': 10, 'H': 10},
        'G': {'C': 10},
        'H': {'F': 10, 'D': 10},
        'I': {},
    }
    return g


def test_depth_first_method_exist():
    """Test depth method exists"""
    assert Graph.depth_first_graph


def test_depth_first_search_is_successful(graph_filled):
    """Test DFS is successful from the graph"""
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert graph_filled.depth_first_graph('A') == expected


def test_depth_first_search_with_one_node(graph_filled):
    """Test DFS with one node"""
    assert len(graph_filled.depth_first_graph('I')) == 1


def test_depth_first_search_with_empty_graph(graph_empty):
    """Test DFS with an empty graph"""
    with pytest.raises(KeyError):
        assert graph_empty.depth_first_graph('')


def test_vertex_does_not_exist(graph_filled):
    """Test when vertex does not exist in the graph"""
    with pytest.raises(KeyError):
        assert graph_filled.depth_first_graph('J')



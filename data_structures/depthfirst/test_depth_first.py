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
        'A': {'B, D'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'G'},
        'D': {'A', 'B', 'E', 'F', 'H'},
        'E': {'D'},
        'F': {'D', 'H'},
        'G': {'C'},
        'H': {'D', 'F'},
    }
    return g


def test_depth_first_search_is_successful(graph_filled):
    """Test DFS is successful from the graph"""
    assert graph_filled.depth_first_graph('A')


# def test_depth_first_search_with_one_node(graph_filled):
#     """Test DFS with one node"""
#     pass
#
#
# def test_depth_first_search_with_empty_graph(empty_graph):
#     """Test DFS with an empty graph"""
#     pass

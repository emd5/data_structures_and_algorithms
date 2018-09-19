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
        'Pandora': {'Arendelle': 10},
        'Arendelle': {'Pandora': 10, 'Metroville': 10, 'Monstropolis': 10},
        'Metroville': {'Narnia': 10, 'Arendelle': 10, 'Monstropolis': 10, 'Naboo': 10},
        'Monstropolis': {'Arendelle': 10, 'Metroville': 10, 'Naboo': 10},
        'Naboo': {'Monstropolis': 10, 'Metroville': 10, 'Narnia': 10},
        'Narnia': {'Metroville': 10, 'Naboo': 10},
    }
    return g


def test_depth_first_search_is_successful(graph_filled):
    """Test DFS is successful from the graph"""
    pass


def test_depth_first_search_with_one_node(graph_filled):
    """Test DFS with one node"""
    pass


def test_depth_first_search_with_empty_graph(empty_graph):
    """Test DFS with an empty graph"""
    pass

import pytest
from .graph import Graph


@pytest.fixture()
def graph_filled_for_traversal():
    """Set up a graph for traversal."""
    g = Graph()
    g.graph = {
        'Pandora': {'Arendelle': 10,},
        'Arendelle': {'Pandora': 10, 'Metroville': 10, 'Monstropolis': 10},
        'Metroville': {'Narnia': 10, 'Arendelle': 10, 'Monstropolis': 10, 'Naboo': 10},
        'Monstropolis': {'Arendelle': 10, 'Metroville': 10, 'Naboo': 10},
        'Naboo': {'Monstropolis': 10, 'Metroville': 10, 'Narnia': 10},
        'Narnia': {'Metroville': 10, 'Naboo': 10},
        'Single': {}
    }
    return g


@pytest.fixture()
def empty_graph():
    """Set up an empty graph"""
    g = Graph()
    g.graph = {}
    return g


def test_breadth_first_graph_traverse_success(graph_filled_for_traversal):
    """Test BFS traverses properly through the graph"""
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstropolis', 'Narnia', 'Naboo']
    actual = graph_filled_for_traversal.breadth_first_graph('Pandora')
    assert actual == expected


def test_breadth_first_traverse_different_path_success(graph_filled_for_traversal):
    """Test BFS traverses with a different path through the graph"""
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstropolis', 'Narnia', 'Naboo']
    actual = graph_filled_for_traversal.breadth_first_graph('Pandora')
    assert actual == expected


def test_bfs_with_one_node(graph_filled_for_traversal):
    """Test for single node with no edges or neighbors"""
    with pytest.raises(TypeError):
        assert graph_filled_for_traversal.breadth_first_graph('Single')


def test_bfs_with_empty_graph(empty_graph):
    """Test bfs with empty graph """
    with pytest.raises(TypeError):
        assert empty_graph.breadth_first_graph()




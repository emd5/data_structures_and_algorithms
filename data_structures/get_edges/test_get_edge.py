import pytest
from .graph import Graph


@pytest.fixture()
def setup_graph():
    """Set up a graph for traversal."""
    g = Graph()
    g.graph = {
        'Pandora': {'Arendelle': 150,},
        'Arendelle': {'Pandora': 150, 'Metroville': 82, 'Monstropolis': 105},
        'Metroville': {'Narnia': 37, 'Arendelle': 82, 'Monstropolis': 105, 'Naboo': 26},
        'Monstropolis': {'Arendelle': 42, 'Metroville': 105, 'Naboo': 73},
        'Naboo': {'Monstropolis': 73, 'Metroville': 26, 'Narnia': 250},
        'Narnia': {'Metroville': 37, 'Naboo': 250},
        'Single': {}
    }
    return g


@pytest.fixture()
def empty_graph():
    """Set up an empty graph"""
    g = Graph()
    g.graph = {}
    return g


def test_get_edge_is_pandora_to_pandora(setup_graph):
    """Test BFS traverses properly through the graph"""
    assert setup_graph.get_edges(['Pandora', 'Arendelle', 'Pandora']) == [True, 300]


def test_get_edge_with_path(setup_graph):
    """Test a successful path"""
    citylist = ['Arendelle', 'Monstropolis', 'Naboo']
    assert setup_graph.get_edges(citylist) == [True, 178]


def test_get_edge_fails(setup_graph):
    """Test a nonexistent vertex and fails """
    citylist = ['Arendelle', 'North Pole']
    assert setup_graph.get_edges(citylist) == [False, 0]

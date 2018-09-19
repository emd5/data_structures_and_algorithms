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


def test_same_source_and_destination_is_successful(setup_graph):
    """Test BFS traverses properly through the graph"""
    assert setup_graph.get_edges(['Pandora', 'Arendelle', 'Pandora']) == [True, 300]


def test_get_edge_with_path_is_successful(setup_graph):
    """Test a successful path"""
    citylist = ['Arendelle', 'Monstropolis', 'Naboo']
    assert setup_graph.get_edges(citylist) == [True, 178]


def test_nonexistent_vertex_destination_fails(setup_graph):
    """Test a nonexistent vertex and fails """
    citylist = ['Arendelle', 'North Pole']
    assert setup_graph.get_edges(citylist) == [False, 0]


def test_nonexistent_source_to_existent_destination_fails(setup_graph):
    """Test a nonexistent source to a city in a graph, failed result due to KeyError"""
    with pytest.raises(KeyError):
        citylist = ['North Pole', 'Arendelle']
        assert setup_graph.get_edges(citylist)


def test_get_edge_with_empty_fails(empty_graph):
    """Test get edge with empty graph, returns false"""
    assert empty_graph.get_edges([]) == [False, 0]


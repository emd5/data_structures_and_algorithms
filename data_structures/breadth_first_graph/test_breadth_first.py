import pytest
from .graph import Graph


@pytest.fixture()
def graph_filled_for_traversal():
    """Set up a graph for traversal."""
    g = Graph()
    g.graph = {
        'Pandora': {'Arendelle': 10,},
        'Arendelle': {'Pandora': 15, 'Metroville': 5, 'Monstropolis': 2},
        'Metroville': {'Narnia': 50, 'Arendelle': 25, 'Monstropolis': 10, 'Naboo': 10},
        'Monstropolis': {'Arendelle': 5, 'Metroville': 10, 'Naboo': 4},
        'Naboo': {'Monstropolis': 5, 'Metroville':10, 'Narnia': 8},
        'Narnia': {'Metroville': 10, 'Naboo': 20},
    }
    return g


def test_breadth_first_graph_is_empty(graph_filled_for_traversal):
    assert graph_filled_for_traversal.breadth_first_graph('Pandora')

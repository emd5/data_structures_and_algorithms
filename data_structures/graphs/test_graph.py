import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    """Set up an empty graph"""
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    """Set up a graph with vertices"""
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    """Set up a graph for traversal."""
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


def test_has_vert(graph_filled):
    """Test the value D exist in graph."""
    assert graph_filled.has_vert('D') is True


def test_does_not_have_vert(graph_filled):
    """Test the value Z does not exist in graph."""
    assert graph_filled.has_vert('Z') is False


def test_has_vert_with_int(graph_filled):
    """Test an integer does not exist in graph."""
    assert graph_filled.has_vert(1) is False


def test_add_vert_fails(graph_filled):
    """Test add existing vertex fails."""
    actual = 'Already has the vertex!'
    assert graph_filled.add_vert('A') == actual


def test_add_vert_successful(graph_filled):
    """Test add value G is successful"""
    graph_filled.add_vert('G')
    assert graph_filled.has_vert('G') is True


def test_add_vert_empty_graph(graph_empty):
    """Test add value G value to an empty graph is  successful"""
    assert len(graph_empty) == 0
    graph_empty.add_vert('A')
    assert len(graph_empty) == 1


def test_add_edge_successful(graph_filled):
    """Test add edge is successful."""
    graph_filled.add_edge('A', 'G', 4)
    assert graph_filled.graph['A']['G'] == 4


def test_add_edge_with_existing_edge(graph_filled):
    """Test add edge with an existing two vertices and edge."""
    assert graph_filled.add_edge('A', 'B', 10) == 'Edge already exist'


def test_add_edge_with_no_vertex(graph_filled):
    """Test add edge with no vertex in the graph"""
    assert graph_filled.add_edge('Z', 'B', 11) == 'No Vertex found'


def test_get_neighbors_is_successful(graph_filled_for_traversal):
    """Test get neighbors from A, which is B and C"""
    neighbors = graph_filled_for_traversal.get_neighbors('A')
    assert neighbors == ['B', 'C']


def test_get_neighbors_fails(graph_filled_for_traversal):
    """Test get neighbors and returns no neighbors found."""
    neighbors = graph_filled_for_traversal.get_neighbors('D')
    assert neighbors == 'No neighbors found.'


def test_get_neighbors_with_no_vertex(graph_filled_for_traversal):
    """Test get neighbors with no vertex in the graph"""
    assert graph_filled_for_traversal.get_neighbors('Z') == 'No Vertex found'


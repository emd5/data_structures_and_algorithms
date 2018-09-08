class Graph:
    def __init__(self):
        """Set up an empty graph"""
        self.graph = {}

    def __repr__(self):
        """Set up a graph with vertices"""
        pass

    def __str__(self):
        """An official String representation of the vertice object"""
        pass

    def __len__(self):
        """Length of the graph"""
        return len(self.graph)

    def add_vert(self, val):
        """Add vertex as a value."""
        if val not in self.graph:
            self.graph['val'] = val

    def has_vert(self, val):
        """A helper method to check for existing vertices."""
        for vertex in self.graph.items():
            if val is vertex:
                return True
        return False

    def add_edge(self, v1, v2, weight):
        """Adds an edge when two vertices are present, edge has a weight."""

        if v2 not in self.graph[v1]:
            self.graph[v1].update({v2: weight})
        else:
            raise Exception

    def get_neighbors(self, val):
        """"""
        # if val is self.graph:









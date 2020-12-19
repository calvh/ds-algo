from data_structures.AdjacencyListGraph import *


class AdjacencyListUndirectedGraph(AdjacencyListGraph):
    """Undirected graph implemented with an adjacency list"""

    def remove_vertex(self, v):

        # check if vertex exists
        if v not in self.vertices:
            raise ValueError(f"Vertex {v} does not exist.")

        # find connected vertices and edge references
        for u in self.vertices[v]["out"]:
            self.vertices[u]["out"].remove(v)

        # remove associated edges
        for e in self.incident_edges(v):
            self.remove_edge(e[0], e[1])

        return self.vertices.pop(v)

    def edge_exists(self, v1, v2):
        return (v1, v2) in self.edges or (v2, v1) in self.edges

    def get_edge(self, v1, v2):

        if self.edge_exists(v1, v2) is True:
            try:
                return self.edges[(v1, v2)]
            except KeyError:
                return self.edges[(v2, v1)]

    def add_edge(self, v1, v2, **kwargs):

        # check if vertices exist
        if v1 not in self.vertices:
            raise ValueError(f"Vertex {v1} does not exist.")
        if v2 not in self.vertices:
            raise ValueError(f"Vertex {v2} does not exist.")

        # check if edge already exists
        if self.edge_exists(v1, v2) is True:
            raise ValueError(f"Edge ({v1}, {v2}) already exists")

        # edge does not exist yet
        # add reference in edges
        self.edges[(v1, v2)] = kwargs

        # add reference in vertices
        # undirected graph only uses "out" list
        self.vertices[v1]["out"].add(v2)
        self.vertices[v2]["out"].add(v1)

    def remove_edge(self, v1, v2):

        # check if edge exists
        if self.edge_exists(v1, v2) is False:
            raise ValueError(f"Edge ({v1}, {v2}) does not exist")

        # edge exists
        e = self.get_edge(v1, v2)
        del e

        # remove edge in adjacency lists
        self.vertices[v1]["out"].remove(v2)
        self.vertices[v2]["out"].remove(v1)

        return (v1, v2)

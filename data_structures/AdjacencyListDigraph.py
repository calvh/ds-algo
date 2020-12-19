from data_structures.AdjacencyListGraph import *

class AdjacencyListDigraph(AdjacencyListGraph):
    """Digraph implemented with an adjacency list"""

    def remove_vertex(self, v):

        # check if vertex exists
        if v not in self.vertices:
            raise ValueError(f"Vertex with {v} does not exist.")

        # remove vertex from the adjacency lists of connected vertices
        for v in self.vertices[v]["in"]:
            self.vertices[v]["out"].remove(v)

        for v in self.vertices[v]["out"]:
            self.vertices[v]["in"].remove(v)

        # remove associated edges
        for e in self.get_incident_edges(v):
            self.remove_edge(e[0], e[1])

        return self.vertices.pop(v)

    def find_edge(self, v1, v2):

        try:
            return self.edges[(v1, v2)]
        except KeyError:
            return False

    def add_edge(self, v1, v2, **kwargs):

        # check if vertex keys are valid
        if v1 not in self.vertices:
            raise ValueError(f"Vertex {v1} does not exist.")
        if v2 not in (self.vertices):
            raise ValueError(f"Vertex {v2} does not exist.")

        # check if edge already exists
        if self.find_edge(v1, v2) is not False:
            raise ValueError(f"Edge ({v1}, {v2}) already exists")

        # edge does not exist yet
        # add reference in edges
        self.edges[(v1, v2)] = kwargs

        # add reference in vertices
        self.vertices[v1]["out"].add(v2)
        self.vertices[v2]["in"].add(v1)

    def remove_edge(self, v1, v2):

        # check if edge exists
        e = self.find_edge(v1, v2)
        if e is False:
            raise ValueError(f"Edge ({v1}, {v2}) does not exist")

        # edge exists
        del e

        # remove edge in adjacency lists
        self.vertices[v1]["out"].remove(v2)
        self.vertices[v2]["in"].remove(v1)

        return (v1, v2)

    def reverse_edges(self):

        # todo: use list in case mutating self.edges causes issues with the loop, to be confirmed

        # todo: how to handle parallel edge?

        # make new dictionaries to be safe
        # newVertices = {}
        # newEdges = {}

        return False
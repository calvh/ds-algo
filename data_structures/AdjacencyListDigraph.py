from data_structures.AdjacencyListGraph import *

class AdjacencyListDigraph(AdjacencyListGraph):
    """Digraph implemented with an adjacency list"""

    def remove_vertex(self, key):

        # check if vertex exists
        if key not in self.vertices:
            raise ValueError(f"Vertex with key {key} does not exist.")

        # remove vertex from the adjacency lists of connected vertices
        for v in self.vertices[key]["in"]:
            self.vertices[v]["out"].remove(key)

        for v in self.vertices[key]["out"]:
            self.vertices[v]["in"].remove(key)

        # remove associated edges
        for e in self.get_incident_edges(key):
            self.remove_edge(e[0], e[1])

        return self.vertices.pop(key)

    def find_edge(self, key1, key2):

        try:
            return self.edges[(key1, key2)]
        except KeyError:
            return False

    def add_edge(self, key1, key2, **kwargs):

        # check if vertex keys are valid
        if key1 not in self.vertices:
            raise ValueError(f"Vertex {key1} does not exist.")
        if key2 not in (self.vertices):
            raise ValueError(f"Vertex {key2} does not exist.")

        # check if edge already exists
        if self.find_edge(key1, key2) is not False:
            raise ValueError(f"Edge ({key1}, {key2}) already exists")

        # edge does not exist yet
        # add reference in edges
        self.edges[(key1, key2)] = kwargs

        # add reference in vertices
        self.vertices[key1]["out"].add(key2)
        self.vertices[key2]["in"].add(key1)

    def remove_edge(self, key1, key2):

        # check if edge exists
        e = self.find_edge(key1, key2)
        if e is False:
            raise ValueError(f"Edge ({key1}, {key2}) does not exist")

        # edge exists
        del e

        # remove edge in adjacency lists
        self.vertices[key1]["out"].remove(key2)
        self.vertices[key2]["in"].remove(key1)

        return (key1, key2)

    def reverse_edges(self):

        # todo: use list in case mutating self.edges causes issues with the loop, to be confirmed

        # todo: how to handle parallel edge?

        # make new dictionaries to be safe
        # newVertices = {}
        # newEdges = {}

        return False
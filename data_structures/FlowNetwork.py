from data_structures.AdjacencyListDigraph import *


class FlowNetwork(AdjacencyListDigraph):
    """Flow network implemented using an adjacency-list-based graph"""

    def __init__(self, digraph, capacity_function, source, sink):

        # todo find out more on this
        # self.capacity_function = capacity_function

        self.vertices = digraph.vertices
        self.edges = digraph.edges
        self.source = source
        self.sink = sink

    def set_capacity(self, v1, v2, c):

        if c < 0:
            raise ValueError("Capacity must be non-negative.")
        self.set_edge_field(v1, v2, capacity=c)

    def set_flow(self, v1, v2, f):

        if f > self.get_capacity(v1, v2):
            raise ValueError(
                f"Flow cannot exceed capacity of {self.get_capacity(v1, v2)}"
            )
        self.set_edge_field(v1, v2, flow=f)

    def get_capacity(self, v1, v2):
        return self.get_edge_field(v1, v2, "capacity")

    def get_flow(self, v1, v2):
        return self.get_edge_field(v1, v2, "flow")
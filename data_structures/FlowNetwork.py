from data_structures.AdjacencyListDigraph import *


class FlowNetwork(AdjacencyListDigraph):
    """Flow network implemented using an adjacency-list-based graph"""

    def __init__(self, digraph, capacities, source, sink):

        self.vertices = digraph.vertices
        self.edges = digraph.edges

        self.source = source
        self.sink = sink

        # the capacity function specified in the parameter capacities is a dictionary which maps edges (tuples) to capacities
        self.capacities = capacities

    def set_capacity(self, v1, v2, c):

        if c < 0:
            raise ValueError("Capacity must be non-negative.")

        self.capacities[(v1, v2)] = c

    def get_capacity(self, v1, v2):
        return self.capacities[(v1, v2)]

    def set_flow(self, v1, v2, f):

        if f > self.capacities[(v1, v2)]:
            raise ValueError(
                f"Flow cannot exceed capacity of {self.capacities[(v1, v2)]}"
            )
        self.set_edge_field(v1, v2, flow=f)

    def get_flow(self, v1, v2):
        return self.get_edge_field(v1, v2, "flow")
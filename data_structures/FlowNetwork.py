from data_structures.AdjacencyListDigraph import *
from copy import deepcopy


class FlowNetwork(AdjacencyListDigraph):
    """Flow network implemented using an adjacency-list-based graph"""

    def __init__(self, digraph, capacities, source, sink, flow=None):
        
        self.source = source
        self.sink = sink

        # deepcopy to reduce probability of errors

        self.vertices = deepcopy(digraph).vertices
        self.edges = deepcopy(digraph).edges

        # the capacity function specified in the parameter capacities is a dictionary which maps edges (tuples) to capacities
        self.capacities = deepcopy(capacities)

        # allow user to set initial flow
        self.flow = {} if flow is None else deepcopy(flow)

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
        self.flow[(v1, v2)] = f

    def get_flow(self, v1, v2):
        return self.flow[(v1, v2)]
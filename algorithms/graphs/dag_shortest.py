from algorithms.graphs.topological_sort import *
import math


def dag_shortest(g, s):

    # todo store distance in dictionary

    order = topological_sort(g)

    if order is False:
        # digraph has a directed cycle
        return

    # convenience functions
    def get_distance(vertex):
        return g.get_vertex_field(vertex, "distance")

    def set_distance(vertex, distance):
        g.set_vertex_field(vertex, distance=distance)

    def get_weight(vertex1, vertex2):
        return g.get_edge_field(vertex1, vertex2, "weight")

    for vertex in g.get_vertices():
        set_distance(vertex, math.inf)

    set_distance(s, 0)

    for i in range(g.size() - 1):

        for v_i, u in g.outgoing_edges(order[i]):

            new_distance = get_distance(v_i) + get_weight(v_i, u)

            if new_distance < get_distance(u):
                set_distance(u, new_distance)
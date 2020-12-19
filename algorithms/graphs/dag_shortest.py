from algorithms.graphs.topological_sort import *
import math


def dag_shortest(g, s):

    order = topological_sort(g)

    if order is False:
        # digraph has a directed cycle
        return

    distances = {}

    for vertex in g.get_vertices():
        distances[vertex] = math.inf

    distances[s] = 0

    for i in range(g.size() - 1):

        for v_i, u in g.outgoing_edges(order[i]):

            new_distance = distances[v_i] + g.get_edge_field(v_i, u, "weight")

            if new_distance < distances[u]:
                distances[u] = new_distance

    return distances
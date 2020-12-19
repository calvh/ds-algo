from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph
from data_structures.Stack import Stack
from collections import deque


def topological_sort(g):

    stack = deque()
    order = []
    in_counter = {}

    for u in g.get_vertices():
        in_counter[u] = g.in_degree(u)
        if in_counter[u] == 0:
            stack.append(u)

    while len(stack) > 0:

        u = stack.pop()
        order.append(u)

        for e in g.outgoing_edges(u):

            w = g.opposite(u, e)
            in_counter[w] = in_counter[w] - 1

            if in_counter[w] == 0:
                stack.append(w)

    # Digraph has no directed cycles
    if len(order) == len(g.get_vertices()):
        return order

    # Digraph has a directed cycle
    return False

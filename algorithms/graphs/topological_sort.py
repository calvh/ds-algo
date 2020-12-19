from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph
from data_structures.Stack import Stack
from collections import deque


def topological_sort(g):

    stack = deque()
    vertices = []

    for u in g.get_vertices():
        in_degree = g.in_degree(u)
        g.set_vertex_field(u, in_counter=in_degree)
        if g.get_vertex_field(u, "in_counter") == 0:
            stack.append(u)

    while len(stack) > 0:

        u = stack.pop()
        vertices.append(u)

        for e in g.outgoing_edges(u):

            w = g.opposite(u, e)
            in_counter = g.get_vertex_field(w, "in_counter") - 1
            g.set_vertex_field(w, in_counter=in_counter)

            if in_counter == 0:
                stack.append(w)

    if len(vertices) == len(g.get_vertices()):
        return vertices
    return "Digraph has a directed cycle."

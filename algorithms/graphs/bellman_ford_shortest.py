import math


def bellman_ford_shortest(g, v):

    # convenience functions
    def get_distance(vertex):
        return g.get_vertex_field(vertex, "distance")

    def set_distance(vertex, distance):
        g.set_vertex_field(vertex, distance=distance)

    def get_weight(vertex1, vertex2):
        return g.get_edge_field(vertex1, vertex2, "weight")

    for vertex in g.get_vertices():
        set_distance(vertex, math.inf)

    set_distance(v, 0)

    for i in range(g.size()):

        done = True

        for u, z in g.get_edges():

            new_distance = get_distance(u) + get_weight(u, z)

            if new_distance < get_distance(z):
                done = False
                set_distance(z, new_distance)

    if done is True:
        return "Complete"
    else:
        return "G contains a negative-weight cycle"

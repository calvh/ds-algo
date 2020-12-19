import math


def bellman_ford_shortest(g, v):

    distances = {}

    for vertex in g.get_vertices():
        distances[vertex] = math.inf

    distances[v] = 0

    for i in range(g.size()):

        done = True

        for u, z in g.get_edges():

            new_distance = distances[u] + g.get_edge_field(u, z, "weight")

            if new_distance < distances[z]:
                done = False
                distances[z] = new_distance

    if done is True:
        return distances
    else:
        # G contains a negative-weight cycle
        return False

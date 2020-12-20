import math


def allpairs_shortest(g):

    vertices = g.get_vertices()
    n = range(len(vertices))

    distances = [[None for i in n] for i in n]

    for i in n:
        for j in n:
            if i == j:
                distances[i][i] = 0
            elif g.edge_exists(vertices[i], vertices[j]) is True:
                distances[i][j] = g.get_edge_field(vertices[i], vertices[j], "weight")
            else:
                distances[i][j] = math.inf


    for k in n:

        new_distances = [[None for i in n] for i in n]

        for i in n:
            for j in n:
                new_distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )

        distances = new_distances

    new_distances.append(vertices)
    return new_distances

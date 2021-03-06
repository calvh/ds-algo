from copy import deepcopy


def floyd_warshall(g):

    v = g.get_vertices()
    n = range(len(v))

    g_prev = g

    for k in n:

        g_current = deepcopy(g_prev)

        for i in [i for i in n if i != k]:
            for j in [j for j in n if (j != k and j != i)]:
                if (g_prev.edge_exists(v[i], v[k]) is True) and (
                    g_prev.edge_exists(v[k], v[j]) is True
                ):
                    if g_current.edge_exists(v[i], v[j]) is False:
                        g_current.add_edge(v[i], v[j])

        g_prev = g_current

    return g_current

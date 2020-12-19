def bfs_directed_at(g, s):
    """
    perform DFS on an undirected graph g starting at s
    """
    lists = [[]]
    g.set_vertex_field(s, explored=True)
    i = 0

    lists[i].append(s)

    while len(lists[i]) > 0:
        lists.append([])
        for v in lists[i]:
            for e in g.outgoing_edges(v):
                if g.get_edge_field(*e, "explored") is False:
                    g.set_edge_field(*e, explored=True)
                    w = e[1] if (e[0] == v) else e[0]
                    if g.get_vertex_field(w, "explored") is False:
                        g.set_edge_field(*e, label="discovery")
                        g.set_vertex_field(w, explored=True)
                        lists[i + 1].append(w)
                    else:
                        g.set_edge_field(*e, label="crossedge")
        i += 1

    lists.pop()  # this is an empty list

    return lists

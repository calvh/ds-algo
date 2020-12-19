def dfs_undirected(g):
    """
    perform DFS on an undirected graph g
    """
    for v in g.get_vertices():
        if g.get_vertex_field(v, "explored") is False:
            dfs_undirected_at(g, v)


def dfs_undirected_at(g, v):
    """
    perform DFS on an undirected graph g starting at v
    """
    g.set_vertex_field(v, explored=True)
    for e in g.incident_edges(v):
        if g.get_edge_field(*e, "explored") is False:
            g.set_edge_field(*e, explored=True)
            w = e[1] if (e[0] == v) else e[0]  # w is the other end of the edge
            if g.get_vertex_field(w, "explored") is False:
                g.set_edge_field(*e, label="discovery")
                dfs_undirected_at(g, w)
            else:
                g.set_edge_field(*e, label="backedge")

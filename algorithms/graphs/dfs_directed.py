def dfs_directed_at(g, v):
    """
    perform DFS on an directed graph g starting at v

    active: tracks vertices which have not finished exploring all their outgoing edges
    """
    g.set_vertex_field(v, active=True)

    for e in g.outgoing_edges(v):
        if g.get_edge_field(*e, "explored") is False:

            g.set_edge_field(*e, explored=True)
            w = e[1]  # w is the destination of e

            isExplored = g.get_vertex_field(w, "explored")
            isActive = g.get_vertex_field(w, "active")

            if (isExplored is False) and (isActive is False):
                # unexplored and inactive
                g.set_edge_field(*e, label="discovery")
                dfs_directed_at(g, w)
            elif isActive is True:
                # explored and active
                g.set_edge_field(*e, label="backedge")  # ancestor
            else:
                # explored but inactive
                g.set_edge_field(*e, label="forward/crossedge")  # descendant or sibling

    g.set_vertex_field(v, explored=True, active=False)

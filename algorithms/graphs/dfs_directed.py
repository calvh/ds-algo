from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph


def dfs_directed_at(g, v):
    """
    perform DFS on an directed graph g starting at v

    active: tracks vertices which have not finished exploring all their outgoing edges
    """
    g.set_vertex_field(v, active=True)

    for e in g.get_outgoing_edges(v):
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


g = Graph()

g.add_vertex("BOS", "BOS", explored=False, active=False)
g.add_vertex("JFK", "JFK", explored=False, active=False)
g.add_vertex("DFW", "DFW", explored=False, active=False)
g.add_vertex("LAX", "LAX", explored=False, active=False)
g.add_vertex("ORD", "ORD", explored=False, active=False)
g.add_vertex("SFO", "SFO", explored=False, active=False)
g.add_vertex("MIA", "MIA", explored=False, active=False)

g.add_edge("BOS", "JFK", explored=False)
g.add_edge("BOS", "SFO", explored=False)
g.add_edge("BOS", "MIA", explored=False)
g.add_edge("JFK", "BOS", explored=False)
g.add_edge("JFK", "DFW", explored=False)
g.add_edge("JFK", "SFO", explored=False)
g.add_edge("JFK", "MIA", explored=False)
g.add_edge("DFW", "ORD", explored=False)
g.add_edge("DFW", "SFO", explored=False)
g.add_edge("DFW", "LAX", explored=False)
g.add_edge("ORD", "DFW", explored=False)
g.add_edge("ORD", "MIA", explored=False)
g.add_edge("MIA", "DFW", explored=False)
g.add_edge("MIA", "LAX", explored=False)
g.add_edge("LAX", "ORD", explored=False)

dfs_directed_at(g, "BOS")
print(g)
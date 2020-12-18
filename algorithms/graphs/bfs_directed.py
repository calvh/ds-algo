from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph

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
            for e in g.get_outgoing_edges(v):
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


g = Graph()

g.add_vertex("BOS", "BOS", explored=False)
g.add_vertex("JFK", "JFK", explored=False)
g.add_vertex("DFW", "DFW", explored=False)
g.add_vertex("LAX", "LAX", explored=False)
g.add_vertex("ORD", "ORD", explored=False)
g.add_vertex("SFO", "SFO", explored=False)
g.add_vertex("MIA", "MIA", explored=False)

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

l = bfs_directed_at(g, "BOS")
print(g)
print(l)
import sys

sys.path.append("/home/calvin/work/ds-algo/")
from data_structures.AdjacencyListGraph import AdjacencyListGraph as Graph
from string import ascii_uppercase


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
    for e in g.get_incident_edges(v):
        if g.get_edge_field(*e, "explored") is False:
            g.set_edge_field(*e, explored=True)
            w = e[1] if (e[0] == v) else e[0]  # w is the other end of the edge
            if g.get_vertex_field(w, "explored") is False:
                g.set_edge_field(*e, label="discovery")
                dfs_undirected_at(g, w)
            else:
                g.set_edge_field(*e, label="backedge")


g = Graph()

for c in ascii_uppercase:
    if c == "Q":
        break
    g.add_vertex(c, c, explored=False)

g.add_edge("A", "B", explored=False)
g.add_edge("A", "E", explored=False)
g.add_edge("A", "F", explored=False)
g.add_edge("B", "F", explored=False)
g.add_edge("B", "C", explored=False)
g.add_edge("C", "G", explored=False)
g.add_edge("C", "D", explored=False)
g.add_edge("D", "G", explored=False)
g.add_edge("D", "H", explored=False)
g.add_edge("E", "F", explored=False)
g.add_edge("E", "I", explored=False)
g.add_edge("F", "I", explored=False)
g.add_edge("G", "J", explored=False)
g.add_edge("G", "K", explored=False)
g.add_edge("G", "L", explored=False)
g.add_edge("H", "L", explored=False)
g.add_edge("I", "J", explored=False)
g.add_edge("I", "M", explored=False)
g.add_edge("I", "N", explored=False)
g.add_edge("J", "K", explored=False)
g.add_edge("K", "N", explored=False)
g.add_edge("K", "O", explored=False)
g.add_edge("L", "P", explored=False)
g.add_edge("M", "N", explored=False)
g.add_edge("O", "P", explored=False)

dfs_undirected(g)
print(g)
from data_structures.AdjacencyListGraph import AdjacencyListGraph as Graph
from string import ascii_uppercase


def bfs_undirected_at(g, s):
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
            for e in g.get_incident_edges(v):
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

l = bfs_undirected_at(g, "A")
print(g)
print(l)
from data_structures.AdjacencyListUndirectedGraph import AdjacencyListUndirectedGraph as Graph
from algorithms.graphs.bfs_undirected import *

g = Graph()

for c in "ABCDEFGHIJKLMNOP":
    g.add_vertex(c, explored=False)

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
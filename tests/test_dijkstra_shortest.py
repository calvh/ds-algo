from algorithms.graphs.dijkstra_shortest import *
from data_structures.AdjacencyListUndirectedGraph import *

g = AdjacencyListUndirectedGraph()

for c in "ABCDEFGHI":
    g.add_vertex(c)

g.add_edge("A", "B", weight=13)
g.add_edge("A", "C", weight=6)
g.add_edge("A", "D", weight=4)
g.add_edge("B", "D", weight=6)
g.add_edge("B", "E", weight=2)
g.add_edge("C", "D", weight=1)
g.add_edge("C", "H", weight=8)
g.add_edge("D", "F", weight=3)
g.add_edge("D", "G", weight=20)
g.add_edge("E", "G", weight=6)
g.add_edge("F", "H", weight=10)
g.add_edge("F", "I", weight=2)

dijkstra_shortest(g, "A")

print(g)
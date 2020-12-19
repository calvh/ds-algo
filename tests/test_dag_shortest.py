from algorithms.graphs.dag_shortest import *
from data_structures.AdjacencyListDigraph import *

g = AdjacencyListDigraph()

for i in range(1, 7):
    g.add_vertex(i)

g.add_edge(1, 2, weight=12)
g.add_edge(1, 3, weight=14)
g.add_edge(2, 4, weight=-3)
g.add_edge(2, 5, weight=10)
g.add_edge(3, 4, weight=6)
g.add_edge(3, 5, weight=4)
g.add_edge(4, 5, weight=5)
g.add_edge(4, 6, weight=4)
g.add_edge(5, 6, weight=-2)

dag_shortest(g, 1)

print(g)
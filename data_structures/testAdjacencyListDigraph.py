from data_structures.AdjacencyListDigraph import *

g = AdjacencyListDigraph()

g.add_vertex(1, "ele1")
g.add_vertex(2, "ele2")
g.add_vertex(3, "ele3")
g.add_vertex(4, "ele4")

g.add_edge(1, 2)
g.add_edge(2, 3)

g.set_edge_field(1, 2, weight=10)
g.set_edge_field(2, 3, label=10)
g.set_vertex_field(1, label="VISITED")
g.set_vertex_field(1, label="UNEXPLORED")

print(g)

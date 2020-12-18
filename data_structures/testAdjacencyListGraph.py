from data_structures.AdjacencyListGraph import *

# test code
g = AdjacencyListGraph()

g.add_vertex(1, "ele1", label="VISITED")
g.add_vertex(2, "ele2")
g.add_vertex(3, "ele3")
g.add_vertex(4, "ele4")

g.remove_vertex(4)

g.add_edge(1, 2, label="UNDIRECTED_EDGE")
g.add_edge(2, 3, weight=3, label="UNDIRECTED")

g.set_edge_field(1, 2, weight=10)
g.set_edge_field(2, 3, label="VISITED")

print(g)
print(g.get_vertices())

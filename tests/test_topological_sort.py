from algorithms.graphs.topological_sort import *
from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph
from copy import deepcopy

g_acyclic = Graph()

g_acyclic.add_vertex("A")
g_acyclic.add_vertex("B")
g_acyclic.add_vertex("C")
g_acyclic.add_vertex("D")
g_acyclic.add_vertex("E")
g_acyclic.add_vertex("F")
g_acyclic.add_vertex("G")
g_acyclic.add_vertex("H")
g_acyclic.add_vertex("I")

g_acyclic.add_edge("A", "C")
g_acyclic.add_edge("A", "D")
g_acyclic.add_edge("B", "D")
g_acyclic.add_edge("B", "F")
g_acyclic.add_edge("C", "D")
g_acyclic.add_edge("C", "E")
g_acyclic.add_edge("C", "H")
g_acyclic.add_edge("D", "F")
g_acyclic.add_edge("E", "G")
g_acyclic.add_edge("F", "G")
g_acyclic.add_edge("F", "I")
g_acyclic.add_edge("G", "I")
g_acyclic.add_edge("H", "I")

g_cycle = deepcopy(g_acyclic)
g_cycle.add_edge("I", "B")

print(topological_sort(g_acyclic))
print(topological_sort(g_cycle))


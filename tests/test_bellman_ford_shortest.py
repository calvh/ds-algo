from algorithms.graphs.bellman_ford_shortest import *
from data_structures.AdjacencyListDigraph import *
from copy import deepcopy

g_acyclic = AdjacencyListDigraph()

for c in "ABCDEF":
    g_acyclic.add_vertex(c)

# test graph with no negative-weight cycle
g_acyclic.add_edge("A", "B", weight=8)
g_acyclic.add_edge("A", "C", weight=-2)
g_acyclic.add_edge("A", "D", weight=4)
g_acyclic.add_edge("B", "E", weight=-2)
g_acyclic.add_edge("C", "B", weight=7)
g_acyclic.add_edge("C", "D", weight=1)
g_acyclic.add_edge("C", "E", weight=3)
g_acyclic.add_edge("D", "F", weight=5)
g_acyclic.add_edge("F", "C", weight=9)

# test graph with negative-weight cycle
g_negative_cycle = deepcopy(g_acyclic)
g_negative_cycle.set_edge_field("C", "D", weight=-1)
g_negative_cycle.set_edge_field("D", "F", weight=-5)
g_negative_cycle.set_edge_field("F", "C", weight=-9)

# acyclic
acyclic_distances = bellman_ford_shortest(g_acyclic, "A")
print(acyclic_distances)
print(g_acyclic)

# negative-weight cycle
negative_cycle_distances = bellman_ford_shortest(g_negative_cycle, "A")
print(negative_cycle_distances)
print(g_negative_cycle)
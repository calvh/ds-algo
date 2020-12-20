from data_structures.AdjacencyListDigraph import *
from data_structures.FlowNetwork import *

g = AdjacencyListDigraph()

for i in range(0, 7):
    g.add_vertex(i)

g.add_edge(0, 1, weight=1)
g.add_edge(0, 2, weight=1)
g.add_edge(0, 3, weight=1)
g.add_edge(1, 3, weight=1)
g.add_edge(1, 4, weight=1)
g.add_edge(2, 3, weight=1)
g.add_edge(2, 5, weight=1)
g.add_edge(3, 4, weight=1)
g.add_edge(3, 6, weight=1)
g.add_edge(4, 6, weight=1)
g.add_edge(5, 6, weight=1)

n = FlowNetwork(g, None, 0, 6)

n.set_capacity(0, 1, 10)
n.set_flow(0, 1, 10)

print(n.get_flow(0, 1))
print(n.get_capacity(0, 1))
print(n)
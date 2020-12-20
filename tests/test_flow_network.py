from data_structures.AdjacencyListDigraph import *
from data_structures.FlowNetwork import *

g = AdjacencyListDigraph()

for i in range(0, 7):
    g.add_vertex(i)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(4, 6)
g.add_edge(5, 6)

capacity_function = {
    (0, 1): 7,
    (0, 2): 6,
    (0, 3): 5,
    (1, 3): 1,
    (1, 4): 2,
    (2, 3): 3,
    (2, 5): 9,
    (3, 4): 5,
    (3, 6): 3,
    (4, 6): 6,
    (5, 6): 8,
}

n = FlowNetwork(g, capacity_function, 0, 6)

n.set_capacity(0, 1, 999)
print(n.get_capacity(0, 1))
print(n)
from data_structures.AdjacencyListDigraph import *
from algorithms.graphs.allpairs_shortest import *
import numpy as np


g = AdjacencyListDigraph()

g.add_vertex("BWI")
g.add_vertex("JFK")
g.add_vertex("MIA")
g.add_vertex("ORD")
g.add_vertex("DFW")
g.add_vertex("LAX")

g.add_edge("BWI", "JFK", weight=10)
g.add_edge("BWI", "MIA", weight=20)
g.add_edge("JFK", "ORD", weight=-8)
g.add_edge("JFK", "DFW", weight=-10)
g.add_edge("MIA", "JFK", weight=-15)
g.add_edge("MIA", "DFW", weight=-25)
g.add_edge("MIA", "LAX", weight=30)
g.add_edge("ORD", "BWI", weight=20)
g.add_edge("ORD", "DFW", weight=-10)
g.add_edge("ORD", "LAX", weight=3)
g.add_edge("DFW", "LAX", weight=12)

distances = allpairs_shortest(g)
print(np.array(distances))
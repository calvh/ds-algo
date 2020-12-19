from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph
from algorithms.graphs.floyd_warshall import *

g = Graph()

g.add_vertex("BOS")
g.add_vertex("JFK")
g.add_vertex("DFW")
g.add_vertex("LAX")
g.add_vertex("ORD")
g.add_vertex("SFO")
g.add_vertex("MIA")

g.add_edge("BOS", "JFK")
g.add_edge("BOS", "MIA")
g.add_edge("JFK", "BOS")
g.add_edge("JFK", "MIA")
g.add_edge("JFK", "DFW")
g.add_edge("JFK", "SFO")
g.add_edge("DFW", "ORD")
g.add_edge("DFW", "SFO")
g.add_edge("DFW", "LAX")
g.add_edge("MIA", "DFW")
g.add_edge("MIA", "LAX")
g.add_edge("LAX", "ORD")

print(g)
print(floyd_warshall(g))
from data_structures.AdjacencyListDigraph import AdjacencyListDigraph as Graph
from algorithms.graphs.bfs_directed import *

g = Graph()

g.add_vertex("BOS", explored=False)
g.add_vertex("JFK", explored=False)
g.add_vertex("DFW", explored=False)
g.add_vertex("LAX", explored=False)
g.add_vertex("ORD", explored=False)
g.add_vertex("SFO", explored=False)
g.add_vertex("MIA", explored=False)

g.add_edge("BOS", "JFK", explored=False)
g.add_edge("BOS", "SFO", explored=False)
g.add_edge("BOS", "MIA", explored=False)
g.add_edge("JFK", "BOS", explored=False)
g.add_edge("JFK", "DFW", explored=False)
g.add_edge("JFK", "SFO", explored=False)
g.add_edge("JFK", "MIA", explored=False)
g.add_edge("DFW", "ORD", explored=False)
g.add_edge("DFW", "SFO", explored=False)
g.add_edge("DFW", "LAX", explored=False)
g.add_edge("ORD", "DFW", explored=False)
g.add_edge("ORD", "MIA", explored=False)
g.add_edge("MIA", "DFW", explored=False)
g.add_edge("MIA", "LAX", explored=False)
g.add_edge("LAX", "ORD", explored=False)

l = bfs_directed_at(g, "BOS")
print(g)
print(l)
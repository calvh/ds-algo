from algorithms.graphs.bellman_ford_shortest import *
from data_structures.AdjacencyListDigraph import AdjacencyListDigraph


def test_acyclic():
    # test graph with no negative-weight cycle
    g = AdjacencyListDigraph()

    for c in "ABCDEF":
        g.add_vertex(c)

    g.add_edge("A", "B", weight=8)
    g.add_edge("A", "C", weight=-2)
    g.add_edge("A", "D", weight=4)
    g.add_edge("B", "E", weight=-2)
    g.add_edge("C", "B", weight=7)
    g.add_edge("C", "D", weight=1)
    g.add_edge("C", "E", weight=3)
    g.add_edge("D", "F", weight=5)
    g.add_edge("F", "C", weight=9)

    # acyclic
    acyclic_distances = bellman_ford_shortest(g, "A")
    print(acyclic_distances)
    print(g)


def test_negative_cycle():
    # test graph with negative-weight cycle

    g = AdjacencyListDigraph()

    for c in "ABCDEF":
        g.add_vertex(c)

    g.add_edge("A", "B", weight=8)
    g.add_edge("A", "C", weight=-2)
    g.add_edge("A", "D", weight=4)
    g.add_edge("B", "E", weight=-2)
    g.add_edge("C", "B", weight=7)
    g.add_edge("C", "E", weight=3)
    g.add_edge("C", "D", weight=-1)
    g.add_edge("D", "F", weight=-5)
    g.add_edge("F", "C", weight=-9)

    # negative-weight cycle
    negative_cycle_distances = bellman_ford_shortest(g, "A")
    print(negative_cycle_distances)
    print(g)


def test_airport():
    # test graph with no negative-weight cycle
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

    distances = bellman_ford_shortest(g, "BWI")
    print(distances)
    print(g)

test_acyclic()
test_negative_cycle()
test_airport()
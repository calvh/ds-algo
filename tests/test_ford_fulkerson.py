from data_structures.AdjacencyListDigraph import *
from data_structures.FlowNetwork import *
from algorithms.graphs.ford_fulkerson import *


def test1():
    g = AdjacencyListDigraph()

    for i in range(7):
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

    flow = {
        (0, 1): 3,
        (0, 2): 0,
        (0, 3): 5,
        (1, 3): 1,
        (1, 4): 2,
        (2, 3): 3,
        (2, 5): 0,
        (3, 4): 5,
        (3, 6): 3,
        (4, 6): 6,
        (5, 6): 0,
    }

    n = FlowNetwork(g, capacity_function, 0, 6)

    max_flow = ford_fulkerson(n)
    [print(f"{key}: {value}") for key, value in max_flow.items()]


def test2():
    g = AdjacencyListDigraph()

    for i in range(7):
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
        (0, 1): 8,
        (0, 2): 7,
        (0, 3): 3,
        (1, 3): 6,
        (1, 4): 4,
        (2, 3): 3,
        (2, 5): 3,
        (3, 4): 5,
        (3, 6): 3,
        (4, 6): 9,
        (5, 6): 8,
    }

    flow = {
        (0, 1): 5,
        (0, 2): 3,
        (0, 3): 2,
        (1, 3): 3,
        (1, 4): 2,
        (2, 3): 0,
        (2, 5): 3,
        (3, 4): 2,
        (3, 6): 3,
        (4, 6): 4,
        (5, 6): 3,
    }

    n = FlowNetwork(g, capacity_function, 0, 6)

    max_flow = ford_fulkerson(n)
    [print(f"{key}: {value}") for key, value in max_flow.items()]


def test3():
    g = AdjacencyListDigraph()

    for i in range(8):
        g.add_vertex(i)

    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 7)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    g.add_edge(3, 5)
    g.add_edge(4, 3)
    g.add_edge(4, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)

    capacity_function = {
        (0, 1): 2,
        (0, 3): 5,
        (0, 5): 7,
        (1, 2): 5,
        (2, 4): 1,
        (2, 7): 6,
        (3, 1): 2,
        (3, 2): 2,
        (3, 5): 2,
        (4, 3): 3,
        (4, 7): 1,
        (5, 6): 3,
        (6, 4): 2,
        (6, 7): 8,
    }

    n = FlowNetwork(g, capacity_function, 0, 7)

    max_flow = ford_fulkerson(n)
    [print(f"{key}: {value}") for key, value in max_flow.items()]


def test_backward_edge():
    g = AdjacencyListDigraph()

    for i in range(7):
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
        (0, 1): 8,
        (0, 2): 7,
        (0, 3): 3,
        (1, 3): 6,
        (1, 4): 4,
        (2, 3): 3,
        (2, 5): 3,
        (3, 4): 5,
        (3, 6): 3,
        (4, 6): 9,
        (5, 6): 8,
    }

    flow = {
        (0, 1): 8,
        (0, 2): 3,
        (0, 3): 3,
        (1, 3): 3,
        (1, 4): 2,
        (2, 3): 0,
        (2, 5): 3,
        (3, 4): 5,
        (3, 6): 3,
        (4, 6): 4,
        (5, 6): 3,
    }

    n = FlowNetwork(g, capacity_function, 0, 6, flow=flow)

    max_flow = ford_fulkerson(n)
    [print(f"{key}: {value}") for key, value in max_flow.items()]


test3()
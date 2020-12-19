from dataclasses import dataclass, field
from typing import Any
from heapq import *
import math


# todo revisit and see if this is necessary
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    vertex: Any = field(compare=False)


def dijkstra_shortest(g, v):

    # todo store distance in dictionary

    # convenience functions
    def get_distance(vertex):
        return g.get_vertex_field(vertex, "distance")

    def set_distance(vertex, distance):
        g.set_vertex_field(vertex, distance=distance)

    def get_weight(vertex1, vertex2):
        return g.get_edge_field(vertex1, vertex2, "weight")

    # priority queue
    pq = []

    for vertex in g.get_vertices():
        set_distance(vertex, math.inf)
        heappush(pq, PrioritizedItem(math.inf, vertex))

    set_distance(v, 0)

    while pq:

        # find the closest vertex not yet in the "cloud" of processed vertices
        prioritized_item = heappop(pq)
        u = prioritized_item.vertex
        adjacent = g.adjacent(u)

        for z in adjacent:

            z_loc = -1

            # look for z in pq
            # todo upgrade to binary search
            for i in range(len(pq)):
                if pq[i].vertex == z:
                    z_loc = i
                    break

            # z is in pq
            if z_loc != -1:

                new_distance = get_distance(u) + get_weight(u, z)

                # perform relaxation on z
                if new_distance < get_distance(z):
                    set_distance(z, new_distance)
                    pq[z_loc] = PrioritizedItem(new_distance, z)
                    heapify(pq)

        # todo print output after each iteration if necessary
        # print(g)

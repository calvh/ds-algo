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

    # priority queue
    pq = []

    distances = {}

    for vertex in g.get_vertices():
        distances[vertex] = math.inf
        heappush(pq, PrioritizedItem(math.inf, vertex))

    distances[v] = 0

    while pq:

        # find the closest vertex not yet in the "cloud" of processed vertices
        prioritized_item = heappop(pq)
        u = prioritized_item.vertex
        adjacent = g.adjacent(u)

        for z in adjacent:

            z_loc = -1

            # look for z in pq
            # todo upgrade to heap search
            for i in range(len(pq)):
                if pq[i].vertex == z:
                    z_loc = i
                    break

            # z is in pq
            if z_loc != -1:

                new_distance = distances[u] + g.get_edge_field(u, z, "weight")

                # perform relaxation on z
                if new_distance < distances[z]:
                    distances[z] = new_distance
                    pq[z_loc] = PrioritizedItem(new_distance, z)
                    heapify(pq)

    return distances

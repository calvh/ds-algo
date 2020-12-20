import math
from copy import deepcopy


def ford_fulkerson(n):

    # get initial flow if available
    if n.flow:
        flow = deepcopy(n.get_flow)
    else:
        flow = {e: 0 for e in n.get_edges()}

    flow["max"] = 0

    # todo find a way to return the edge type and residual capacity along with the path
    def find_augmenting_path():

        # explored must be reset for each iteration of find_augmenting path
        explored = {v: False for v in n.get_vertices()}

        def find_augmenting_path_at(u):
            explored[u] = True

            if u == n.sink:
                return [u]

            for w in n.adjacent(u):

                if explored[w] is True:
                    continue

                if n.edge_exists(u, w) is True:
                    # forward edge
                    e = (u, w)
                    residual_capacity = n.get_capacity(*e) - flow[e]
                else:
                    # backward edge
                    e = (w, u)
                    residual_capacity = flow[e]

                if residual_capacity > 0:

                    # recurse
                    find_path = find_augmenting_path_at(w)

                    if find_path is not False:
                        # managed to reach sink from u
                        return [u] + find_path

            # unable to reach sink from u
            return False

        return find_augmenting_path_at(n.source)

    while True:

        # path is a list of vertices from source to sink
        path = find_augmenting_path()

        if path is False:
            return flow

        edge_type = {}
        path_capacity = math.inf

        for i in range(len(path) - 1):
            # collect edge type information while computing residual capacity of path

            u = path[i]
            w = path[i + 1]

            if n.edge_exists(u, w) is True:
                # forward edge
                e = (u, w)
                residual_capacity = n.get_capacity(*e) - flow[e]
                edge_type[e] = "forward"
            else:
                # backward edge
                e = (w, u)
                residual_capacity = flow[e]
                edge_type[e] = "backward"

            if residual_capacity < path_capacity:
                path_capacity = residual_capacity

        flow["max"] += path_capacity

        # push the residual capacity along the path
        for e in edge_type:
            if edge_type[e] == "forward":
                flow[e] += path_capacity
            else:
                flow[e] -= path_capacity

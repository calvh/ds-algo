class AdjacencyListGraph:
    def __init__(self):

        # vertices is a dictionary
        # vertices: {key: {element: element, in: set(), out: set()}}
        # out: set(keys of vertices)
        self.vertices = {}

        # edges is a dictionary indexed using tuples
        # e.g. self.edges: {(v1, v2): {......}}
        # for an undirected graph {(v1, v2) and {(v2, v1) are equivalent
        # undirected edges may be stored as (key1, key2) or (key2, key1)
        self.edges = {}

    def add_vertex(self, *args, **kwargs):

        if len(args) > 2:
            raise ValueError(f"Too many arguments.")

        v = args[0]
        element = args[0] if len(args) == 1 else args[1]

        # only allow non-duplicate keys
        if v in self.vertices:
            raise ValueError(f"Vertex {v} already exists.")

        # todo update to z = x | y syntax when python 3.9 is available on ubuntu
        self.vertices[v] = {"element": element, "in": set(), "out": set(), **kwargs}

    def set_vertex_field(self, v, **kwargs):

        if v not in self.vertices:
            raise ValueError(f"Vertex {v} does not exist")

        self.vertices[v].update(kwargs)

    def get_vertex_field(self, v, field):

        if v not in self.vertices:
            raise ValueError(f"Vertex {v} does not exist")

        return self.vertices[v][field]

    def get_edge_field(self, v1, v2, field):

        if self.edge_exists(v1, v2) is False:
            raise ValueError(f"Edge ({v1}, {v2}) does not exist")

        e = self.get_edge(v1, v2)

        try:
            return e[field]
        except KeyError:
            raise ValueError(f"Edge ({v1}, {v2}) does not have field: '{field}'")

    def set_edge_field(self, v1, v2, **kwargs):

        if self.edge_exists(v1, v2) is False:
            raise ValueError(f"Edge ({v1}, {v2}) does not exist")

        e = self.get_edge(v1, v2)
        e.update(kwargs)

    def in_degree(self, v):
        return len(self.vertices[v]["in"])

    def out_degree(self, v):
        return len(self.vertices[v]["out"])

    def incident_edges(self, v):
        return self.outgoing_edges(v) + self.incoming_edges(v)

    def outgoing_edges(self, v):
        return [(v, destination) for destination in self.vertices[v]["out"]]

    def incoming_edges(self, v):
        return [(origin, v) for origin in self.vertices[v]["in"]]

    def adjacent(self, v):
        return self.vertices[v]["in"].union(self.vertices[v]["out"])

    def opposite(self, v, e):
        return e[0] if v == e[1] else e[1]

    def get_vertices(self):
        return list(self.vertices)

    def get_edges(self):
        return list(self.edges)

    def iterator_dfs(self):
        # todo
        return iter(list(self.vertices))

    def iterator_bfs(self):
        # todo
        return iter(list(self.vertices))

    def is_connected(self):
        # todo
        return False

    def size(self):
        return len(self.vertices)

    def is_empty(self):
        return len(self.vertices) == 0

    def __str__(self):

        if self.is_empty():
            return "The graph is empty."

        output = "\nVertices:\n"
        for v, fields in self.vertices.items():
            output += f"{v}, {fields}\n"

        output += "\nEdges:\n"

        for e, fields in self.edges.items():
            output += f"{e}, {fields}\n"

        return output
class AdjacencyListGraph:
    """Undirected graph implemented with an adjacency list"""

    def __init__(self, vertices={}, edges={}):

        # vertices is a dictionary
        # vertices: {key: {element: element, out: set()}}
        # out: set({keys of vertices})
        self.vertices = vertices

        # edges is a dictionary indexed using tuples
        # e.g. self.edges: {(v1, v2): {......}}
        # for an undirected graph {(v1, v2) and {(v2, v1) are equivalent
        # undirected edges may be stored as (key1, key2) or (key2, key1)
        self.edges = edges

    def add_vertex(self, key, element, **kwargs):

        # only allow non-duplicate keys
        if key in self.vertices:
            raise ValueError(f"Vertex with key {key} already exists.")

        # todo update to z = x | y syntax when python 3.9 is available on ubuntu
        self.vertices[key] = {"element": element, "in": set(), "out": set(), **kwargs}

    def remove_vertex(self, key):

        # check if vertex exists
        if key not in self.vertices:
            raise ValueError(f"Vertex with key {key} does not exist.")

        # find connected vertices and edge references
        for v in self.vertices[key]["out"]:
            self.vertices[v]["out"].remove(key)

        # remove associated edges
        for e in self.get_incident_edges(key):
            self.remove_edge(e[0], e[1])

        return self.vertices.pop(key)

    def find_edge(self, key1, key2):

        try:
            return self.edges[(key1, key2)]
        except KeyError:
            pass

        try:
            return self.edges[(key2, key1)]
        except KeyError:
            return False

    def add_edge(self, key1, key2, **kwargs):

        # check if vertices exist
        if key1 not in self.vertices:
            raise ValueError(f"Vertex {key1} does not exist.")
        if key2 not in self.vertices:
            raise ValueError(f"Vertex {key2} does not exist.")

        # check if edge already exists
        if self.find_edge(key1, key2) is not False:
            raise ValueError(f"Edge ({key1}, {key2}) already exists")

        # edge does not exist yet
        # add reference in edges
        self.edges[(key1, key2)] = kwargs

        # add reference in vertices
        # undirected graph only uses "out" list
        self.vertices[key1]["out"].add(key2)
        self.vertices[key2]["out"].add(key1)

    def remove_edge(self, key1, key2):

        # check if edge exists
        e = self.find_edge(key1, key2)
        if e is False:
            raise ValueError(f"Edge ({key1}, {key2}) does not exist")

        # edge exists
        del e

        # remove edge in adjacency lists
        self.vertices[key1]["out"].remove(key2)
        self.vertices[key2]["out"].remove(key1)

        return (key1, key2)

    def set_vertex_field(self, key, **kwargs):

        if key not in self.vertices:
            raise ValueError(f"Vertex with key {key} does not exist")

        self.vertices[key].update(kwargs)

    def get_vertex_field(self, key, field):

        if key not in self.vertices:
            raise ValueError(f"Vertex with key {key} does not exist")

        return self.vertices[key][field]

    def get_edge_field(self, key1, key2, field):

        e = self.find_edge(key1, key2)
        if e is False:
            raise ValueError(f"Edge ({key1}, {key2}) does not exist")

        try:
            return e[field]
        except KeyError:
            raise ValueError(f"Edge ({key1}, {key2}) does not have field: '{field}'")

    def set_edge_field(self, key1, key2, **kwargs):

        e = self.find_edge(key1, key2)
        if e is False:
            raise ValueError(f"Edge ({key1}, {key2}) does not exist")

        e.update(kwargs)

    def areAdjacent(self, key1, key2):
        return 

    def get_incident_edges(self, key):
        return self.get_outgoing_edges(key) + self.get_incoming_edges(key)

    def get_outgoing_edges(self, key):
        return [(key, destination) for destination in self.vertices[key]["out"]]

    def get_incoming_edges(self, key):
        return [(origin, key) for origin in self.vertices[key]["in"]]

    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return self.edges.keys()

    def iterator_dfs(self):
        # todo
        return []

    def iterator_bfs(self):
        # todo
        return []

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
        for vertex, fields in self.vertices.items():
            output += f"{vertex}, {fields}\n"

        output += "\nEdges:\n"

        for edge, fields in self.edges.items():
            output += f"{edge}, {fields}\n"

        return output
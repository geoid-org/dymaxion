import math

class Icosphere:
    def __init__(self, radius=1, subdivisions=0):
        self.radius = radius
        self.subdivisions = subdivisions
        self.vertices = []
        self.indices = []
        self._init_icosphere()

    def _init_icosphere(self):
        t = (1.0 + math.sqrt(5.0)) / 2.0

        # Add vertices for initial icosahedron
        self.vertices.extend([
            [-1, t, 0],
            [1, t, 0],
            [-1, -t, 0],
            [1, -t, 0],

            [0, -1, t],
            [0, 1, t],
            [0, -1, -t],
            [0, 1, -t],

            [t, 0, -1],
            [t, 0, 1],
            [-t, 0, -1],
            [-t, 0, 1],
        ])

        # Add indices for initial icosahedron
        self.indices.extend([
            [0, 11, 5],
            [0, 5, 1],
            [0, 1, 7],
            [0, 7, 10],
            [0, 10, 11],

            [1, 5, 9],
            [5, 11, 4],
            [11, 10, 2],
            [10, 7, 6],
            [7, 1, 8],

            [3, 9, 4],
            [3, 4, 2],
            [3, 2, 6],
            [3, 6, 8],
            [3, 8, 9],

            [4, 9, 5],
            [2, 4, 11],
            [6, 2, 10],
            [8, 6, 7],
            [9, 8, 1],
        ])

        # Subdivide triangles and normalize vectors to sphere surface
        for _ in range(self.subdivisions):
            self._subdivide()

        for i, v in enumerate(self.vertices):
            length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
            self.vertices[i] = [self.radius * (v[j] / length) for j in range(3)]

    def _subdivide(self):
        indices_new = []
        vertices_len = len(self.vertices)

        for tri in self.indices:
            # create three new vertices in the middle of each triangle edge
            mid = [vertices_len + i for i in range(3)]
            self.vertices.extend([(self.vertices[tri[i]][j] + self.vertices[tri[(i+1)%3]][j]) / 2 for j in range(3)] for i in range(3))

            # create four new triangles for each old one
            indices_new.extend([
                [tri[0], mid[0], mid[2]],
                [tri[1], mid[1], mid[0]],
                [tri[2], mid[2], mid[1]],
                [mid[0], mid[1], mid[2]],
            ])
            vertices_len += 3

        self.indices = indices_new

    def get_vertices(self):
        return self.vertices

    def get_indices(self):
        return self.indices

    def surface_area(self):
        """Return the surface area of the icosphere."""
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        """Return the volume of the icosphere."""
        return (4 / 3) * math.pi * self.radius ** 3

    def distance_from_center(self, vertex_index):
        """Return the distance from the center to the given vertex."""
        vertex = self.vertices[vertex_index]
        return math.sqrt(vertex[0]**2 + vertex[1]**2 + vertex[2]**2)

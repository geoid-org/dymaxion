
import math


class Face:
    def __init__(self, vertices):
        if not all(isinstance(vertex, Vertex) for vertex in vertices):
            raise TypeError("All elements in vertices must be instances of Vertex class.")
        if len(vertices) < 3:
            raise ValueError("A face must be defined by at least 3 non-collinear vertices.")
        self.vertices = vertices

    def edges(self):
        edges = []
        for i in range(len(self.vertices)):
            edges.append(Edge(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)]))
        return edges

    def area(self):
        sum1 = sum(self.vertices[i - 1].x * self.vertices[i].y - self.vertices[i - 1].y * self.vertices[i].x
                   for i in range(len(self.vertices)))
        return abs(sum1) / 2

    def contains_point(self, point):
        inside = False
        for i in range(len(self.vertices)):
            j = (i - 1) % len(self.vertices)
            if ((self.vertices[i].y > point.y) != (self.vertices[j].y > point.y)) and \
               (point.x < self.vertices[i].x + (self.vertices[j].x - self.vertices[i].x) *
                (point.y - self.vertices[i].y) / (self.vertices[j].y - self.vertices[i].y)):
                inside = not inside
        return inside

    def normal(self):
        v1 = self.vertices[1] - self.vertices[0]
        v2 = self.vertices[2] - self.vertices[0]
        return Vertex(v1.y * v2.z - v1.z * v2.y,
                      v1.z * v2.x - v1.x * v2.z,
                      v1.x * v2.y - v1.y * v2.x)

    def centroid(self):
        """Calculate the centroid of the face, which is the average of all the vertices."""
        x_sum = sum(vertex.x for vertex in self.vertices)
        y_sum = sum(vertex.y for vertex in self.vertices)
        z_sum = sum(vertex.z for vertex in self.vertices)
        n = len(self.vertices)
        return Vertex(x_sum / n, y_sum / n, z_sum / n)

    def is_convex(self):
        """Check if the face is convex."""
        # This is a simple method based on the cross product of edges, which might not work correctly for complex polygons
        # A more robust implementation would require advanced algorithms
        n = len(self.vertices)
        vectors = [self.vertices[(i + 1) % n] - self.vertices[i] for i in range(n)]
        cross_products = [vectors[i].cross(vectors[(i + 1) % n]) for i in range(n)]
        dot_products = [cross_products[i].dot(cross_products[(i + 1) % n]) for i in range(n)]
        return all(dp >= 0 for dp in dot_products)

    def get_clockwise_vertices(self):
        """Return a list of all vertices in clockwise order."""
        # This method assumes the vertices are in the plane and seen from the positive side of the normal
        # It uses the atan2 function to calculate the angle of each vertex relative to the centroid
        centroid = self.centroid()
        return sorted(self.vertices, key=lambda vertex: math.atan2(vertex.y - centroid.y, vertex.x - centroid.x))

    def __repr__(self):
        vertices_repr = ', '.join(map(str, self.vertices))
        return f"Face({vertices_repr})"

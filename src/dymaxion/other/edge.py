import math


class Edge:

    def __init__(self, vertex1, vertex2):
        """
        """
        if not isinstance(vertex1, Vertex) or not isinstance(vertex2, Vertex):
            raise TypeError(
                "Both vertex1 and vertex2 must be instances of Vertex class."
            )
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def __repr__(self):
        """
        """
        return f"Edge({self.vertex1}, {self.vertex2})"

    def __eq__(self, other):
        """
        Check if two edges are equal, i.e., they connect the same two vertices.
        """
        if not isinstance(other, Edge):
            return False
        return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or \
               (self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1)

    def length(self):
        return math.sqrt((self.vertex1.x - self.vertex2.x) ** 2 + 
                         (self.vertex1.y - self.vertex2.y) ** 2 + 
                         (self.vertex1.z - self.vertex2.z) ** 2)

    def is_intersecting(self, other):
        v1 = self.vertex2 - self.vertex1
        v2 = other.vertex2 - other.vertex1
        v3 = other.vertex1 - self.vertex1
        cross1 = v1.cross(v2)
        cross2 = v3.cross(v2)
        if cross1.length() == 0 or cross2.length() == 0:
            return False
        t = cross2.dot(cross1) / cross1.length() ** 2
        return 0 <= t <= 1

    def midpoint(self):
        return Vertex((self.vertex1.x + self.vertex2.x) / 2,
                      (self.vertex1.y + self.vertex2.y) / 2,
                      (self.vertex1.z + self.vertex2.z) / 2)

    def direction(self):
        """Calculate the directional vector of the edge."""
        return self.vertex2 - self.vertex1

    def unit_vector(self):
        """Calculate the unit vector in the direction of the edge."""
        dir_vec = self.direction()
        len_vec = self.length()
        return Vertex(dir_vec.x / len_vec, dir_vec.y / len_vec, dir_vec.z / len_vec)


    def angle_between(self, other):
        """
        Calculate the angle between two edges.
        """
        dir_vec1 = self.direction()
        dir_vec2 = other.direction()
        dot_product = dir_vec1.dot(dir_vec2)
        len_product = self.length() * other.length()
        angle_rad = math.acos(dot_product / len_product)
        return math.degrees(angle_rad)

    def is_parallel(self, other):
        """
        Check if two edges are parallel.
        """
        return self.direction().cross(other.direction()).length() == 0

    def is_perpendicular(self, other):
        """
        Check if two edges are perpendicular.
        """
        return self.direction().dot(other.direction()) == 0

    def contains_point(self, point):
        """
        Check if a point lies on the edge.
        """
        dir_vec = self.direction()
        vec_point = point - self.vertex1
        if dir_vec.cross(vec_point).length() != 0:
            return False  # The point is not on the line defined by the edge

        t = vec_point.dot(dir_vec) / self.length() ** 2
        return 0 <= t <= 1  # The point is within the range of the edge


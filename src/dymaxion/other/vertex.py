import math


class Vertex:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        """Return the coordinates of the vertex as a tuple."""
        return self.x, self.y, self.z

    def distance_to(self, other):
        """Calculate the Euclidean distance from this vertex to another."""
        if not isinstance(other, Vertex):
            raise TypeError("Other must be an instance of Vertex class.")
        return math.sqrt((self.x - other.x) ** 2 + 
                         (self.y - other.y) ** 2 + 
                         (self.z - other.z) ** 2)

    def distance_from_origin(self):
        """Calculate the Euclidean distance from this vertex to the origin."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def rotate_x(self, angle):
        """Rotate the vertex around the x-axis by the given angle (in radians)."""
        new_y = self.y * math.cos(angle) - self.z * math.sin(angle)
        new_z = self.y * math.sin(angle) + self.z * math.cos(angle)
        self.y, self.z = new_y, new_z

    def rotate_y(self, angle):
        """Rotate the vertex around the y-axis by the given angle (in radians)."""
        new_x = self.z * math.sin(angle) + self.x * math.cos(angle)
        new_z = self.z * math.cos(angle) - self.x * math.sin(angle)
        self.x, self.z = new_x, new_z

    def rotate_z(self, angle):
        """Rotate the vertex around the z-axis by the given angle (in radians)."""
        new_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        new_y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x, self.y = new_x, new_y

    def __add__(self, other):
        """Add another vertex to this one (vector addition)."""
        if not isinstance(other, Vertex):
            raise TypeError("Can only add another Vertex instance.")
        return Vertex(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Subtract another vertex from this one (vector subtraction)."""
        if not isinstance(other, Vertex):
            raise TypeError("Can only subtract another Vertex instance.")
        return Vertex(self.x - other.x, self.y - other.y, self.z - other.z)

    def __repr__(self):
        return f"Vertex({self.x}, {self.y}, {self.z})"



import math

class Polygon:

    def __init__(self, num_sides, side_length):
        self.n = num_sides
        self.s = side_length

    def perimeter(self):
        """Return the perimeter of the polygon."""
        return self.n * self.s

    def interior_angle(self):
        """Return the measure of each interior angle of the polygon (in degrees)."""
        return (self.n - 2) * 180 / self.n

    def area(self):
        """Return the area of the polygon. Overridden in subclasses."""
        raise NotImplementedError

    def num_sides(self):
        """Return the number of sides in the polygon."""
        return self.n

    def side_length(self):
        """Return the length of a side of the polygon."""
        return self.s

    def __repr__(self):
        return f"Polygon with {self.n} sides of length {self.s}"


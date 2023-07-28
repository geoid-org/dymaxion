
from ._polygon import Polygon

import math

class Square(Polygon):

    def __init__(self, side_length):
        """
        """
        super().__init__(4, side_length)
        self.s = side_length

    def area(self):
        """
        Return the area of the square.
        """
        return self.s ** 2

    def circumradius(self):
        """Return the circumradius of the square."""
        return self.s * math.sqrt(2) / 2

    def inradius(self):
        """Return the inradius of the square."""
        return self.s / 2

    def perimeter(self):
        """Return the perimeter of the square."""
        return self.s * 4

    def semiperimeter(self):
        """Return the semiperimeter of the square."""
        return self.perimeter() / 2

    def apothem(self):
        """Return the apothem of the square."""
        return self.inradius()

    def area_of_each_triangle(self):
        """Return the area of each triangle formed by lines from center to vertices."""
        return self.area() / 4

    def interior_angles(self):
        """Return the measures of the interior angles of the square (in degrees)."""
        # As it's a square, all angles are 90 degrees.
        return [90, 90, 90, 90]  # angles in degrees

    def is_regular(self):
        """Check if the square is regular."""
        # Since all sides and angles are equal in this class, it's always a regular square.
        return True

    def centroid(self):
        """Return the coordinates of the centroid of the square."""
        # For a square centered at the origin, the centroid is also at the origin.
        return (0, 0)

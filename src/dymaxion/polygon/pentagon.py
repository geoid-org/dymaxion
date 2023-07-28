
from ._polygon import Polygon

import math


class Pentagon(Polygon):

    def __init__(self, side_length):
        super().__init__(5, side_length)
        self.s = side_length

    def area(self):
        """Return the area of the pentagon."""
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.s ** 2

    def circumradius(self):
        """Return the circumradius of the pentagon."""
        return (1 / 2) * (1 / math.sin(math.pi / 5)) * self.s

    def inradius(self):
        """Return the inradius of the pentagon."""
        return (1/2) * self.s * math.tan(math.pi / 5)

    def perimeter(self):
        """Return the perimeter of the pentagon."""
        return self.s * 5

    def semiperimeter(self):
        """Return the semiperimeter of the pentagon."""
        return self.perimeter() / 2

    def apothem(self):
        """Return the apothem of the pentagon."""
        return self.inradius()

    def area_of_each_triangle(self):
        """
        Return the area of each triangle formed by lines from center to vertices.
        """
        return self.area() / 5

    def interior_angles(self):
        """Return the measures of the interior angles of the pentagon (in degrees)."""
        # As it's a regular pentagon, all angles are 108 degrees.
        return [108, 108, 108, 108, 108]  # angles in degrees

    def is_regular(self):
        """Check if the pentagon is regular."""
        # Since all sides and angles are equal in this class, it's always a regular pentagon.
        return True

    def centroid(self):
        """Return the coordinates of the centroid of the pentagon."""
        # For a regular pentagon centered at the origin, the centroid is also at the origin.
        return (0, 0)

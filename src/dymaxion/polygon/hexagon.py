
import math


class Hexagon(Polygon):

    def __init__(self, side_length):
        """
        """
        super().__init__(6, side_length)
        self.s = side_length

    def area(self):
        """
        Return the area of the hexagon.
        """
        return (3 * math.sqrt(3) * self.s ** 2) / 2

    def circumradius(self):
        """
        Return the circumradius of the hexagon.
        """
        return self.s

    def inradius(self):
        """
        Return the inradius of the hexagon.
        """
        return self.s * (math.sqrt(3) / 2)

    def perimeter(self):
        """
        Return the perimeter of the hexagon.
        """
        return self.s * 6

    def semiperimeter(self):
        """
        Return the semiperimeter of the hexagon.
        """
        return self.perimeter() / 2

    def apothem(self):
        """
        Return the apothem of the hexagon.
        """
        return self.inradius()

    def area_of_each_triangle(self):
        """
        Return the area of each triangle formed by lines from center
        to vertices.
        """
        return self.area() / 6

    def interior_angles(self):
        """
        Return the measures of the interior angles of the hexagon (in degrees).
        """
        # As it's a regular hexagon, all angles are 120 degrees.
        return [120, 120, 120, 120, 120, 120]  # angles in degrees

    def is_regular(self):
        """
        Check if the hexagon is regular.
        """
        # Since all sides and angles are equal in this class, it's always
        #  a regular hexagon.
        return True

    def centroid(self):
        """
        Return the coordinates of the centroid of the hexagon.
        """
        # For a regular hexagon centered at the origin, the centroid is also
        #  at the origin.
        return (0, 0)

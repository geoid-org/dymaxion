import math

from ._polygon import Polygon


class Triangle(Polygon):
    """
    """

    def __init__(self, side_length):
        super().__init__(3, side_length)
        self.s = side_length

    def area(self) -> float:
        """Return the area of the triangle."""
        return (math.sqrt(3) / 4) * self.s ** 2

    def circumradius(self) -> float:
        """Return the circumradius of the triangle."""
        return self.s / math.sqrt(3)

    def inradius(self) -> float:
        """Return the inradius of the triangle."""
        return self.s / (2 * math.sqrt(3))

    def perimeter(self) -> float:
        """Return the perimeter of the triangle."""
        return self.s * 3

    def semiperimeter(self) -> float:
        """Return the semiperimeter of the triangle."""
        return self.perimeter() / 2

    def height(self) -> float:
        """
        Return the heights of the triangle.
        """
        # In an equilateral triangle, all heights are equal.
        return [(self.s * math.sqrt(3)) / 2] * 3

    @staticmethod
    def interior_angles(self):
        """Return the measures of the interior angles of the triangle (in degrees)."""
        # As it's an equilateral triangle, all angles are 60 degrees.
        return [60, 60, 60]  # angles in degrees

    @staticmethod
    def is_equilateral(self) -> bool:
        """Check if the triangle is equilateral."""
        # Since all sides are equal in this class, it's always an equilateral triangle.
        return True

    def centroid(self):
        """Return the coordinates of the centroid of the triangle."""
        # For an equilateral triangle centered at the origin, the centroid is also at the origin.
        return (0, 0)



# class triangle(Polygon):
#     def __init__(self,a,b,c):
#         Polygon.__init__(self, 3)
#         self.a = a
#         self.b = b
#         self.c = c

#     def area(self):
#         s = (self.a + self.b + self.c)/2
#         area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
#         return area


#     def perimeter(self):
#         return self.a + self.b + self.c

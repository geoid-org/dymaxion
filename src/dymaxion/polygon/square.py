
from ._polygon import Polygon


class Square(Polygon):
    """
    """

    def __init__(self, side_length):
        super().__init__(4, side_length)

    def area(self):
        """Return the area of the square."""
        return self.s ** 2

    def circumradius(self):
        """Return the circumradius of the square."""
        return self.s * math.sqrt(2) / 2


from ._polygon import Polygon

class Triangle(Polygon):
    def __init__(self, side_length):
        super().__init__(3, side_length)

    def area(self):
        """Return the area of the triangle."""
        return (math.sqrt(3) / 4) * self.s ** 2

    def circumradius(self):
        """Return the circumradius of the triangle."""
        return self.s / math.sqrt(3)


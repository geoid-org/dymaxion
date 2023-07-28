

from ._polygon import Polygon

class Hexagon(Polygon):
    def __init__(self, side_length):
        super().__init__(6, side_length)

    def area(self):
        """Return the area of the hexagon."""
        return (3 * math.sqrt(3) * self.s ** 2) / 2

    def circumradius(self):
        """Return the circumradius of the hexagon."""
        return self.s


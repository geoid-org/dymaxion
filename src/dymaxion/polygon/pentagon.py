
from ._polygon import Polygon


class Pentagon(Polygon):
    def __init__(self, side_length):
        super().__init__(5, side_length)

    def area(self):
        """Return the area of the pentagon."""
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.s ** 2

    def circumradius(self):
        """Return the circumradius of the pentagon."""
        return (1/2) * (1/math.sin(math.pi/5)) * self.s

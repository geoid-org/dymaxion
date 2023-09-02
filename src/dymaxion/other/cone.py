
class Cone:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def volume(self):
        """Return the volume of the cone."""
        return (1 / 3) * math.pi * self.r ** 2 * self.h

    def surface_area(self):
        """Return the surface area of the cone."""
        return math.pi * self.r * (self.r + math.sqrt(self.h ** 2 + self.r ** 2))
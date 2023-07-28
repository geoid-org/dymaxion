class Cylinder:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def surface_area(self):
        """Return the surface area of the cylinder."""
        return 2 * math.pi * self.r * (self.r + self.h)

    def volume(self):
        """Return the volume of the cylinder."""
        return math.pi * self.r ** 2 * self.h
class Cube:
    def __init__(self, side_length):
        self.s = side_length

    def volume(self):
        """Return the volume of the cube."""
        return self.s ** 3

    def surface_area(self):
        """Return the surface area of the cube."""
        return 6 * self.s ** 2

    def diagonal(self):
        """Return the length of a diagonal of the cube."""
        return self.s * math.sqrt(3)

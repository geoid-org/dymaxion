class Ellipse:
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.a = semi_major_axis
        self.b = semi_minor_axis

    def area(self):
        """Return the area of the ellipse."""
        return math.pi * self.a * self.b

    def circumference(self):
        """Return the circumference of the ellipse."""
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)

    def focal_length(self):
        """Return the focal length of the ellipse."""
        return 2 * math.sqrt(self.a ** 2 - self.b ** 2)


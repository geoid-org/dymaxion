


import math

class Sphere:
    def __init__(self, radius, center=(0,0,0)):
        self.radius = radius
        self.center = center

    def volume(self):
        """Return the volume of the sphere."""
        return (4/3) * math.pi * self.radius**3

    def surface_area(self):
        """Return the surface area of the sphere."""
        return 4 * math.pi * self.radius**2

    def circumference(self):
        """Return the circumference of the sphere."""
        return 2 * math.pi * self.radius

    def diameter(self):
        """Return the diameter of the sphere."""
        return 2 * self.radius

    def distance_from_center(self, point):
        """Return the distance from the center of the sphere to a given point."""
        return math.sqrt((point[0] - self.center[0])**2 + (point[1] - self.center[1])**2 + (point[2] - self.center[2])**2)

    def is_point_inside(self, point):
        """Check if a given point is inside the sphere."""
        distance = self.distance_from_center(point)
        return distance <= self.radius

    def point_on_surface(self, theta, phi):
        """Return the coordinates of a point on the sphere's surface given spherical coordinates."""
        x = self.radius * math.sin(theta) * math.cos(phi) + self.center[0]
        y = self.radius * math.sin(theta) * math.sin(phi) + self.center[1]
        z = self.radius * math.cos(theta) + self.center[2]
        return x, y, z

    def does_intersect(self, other):
        """Check if another sphere intersects with the sphere."""
        distance_between_centers = self.distance_from_center(other.center)
        return distance_between_centers <= (self.radius + other.radius)

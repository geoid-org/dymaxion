# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Polygon Class
======================

...

Todo:
-----

Links:
------

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Dict, List, Union
import math

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Polygon", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Polygon:
    """
    Polygon Class
    =============
    """

    def __init__(self, num_sides, side_length) -> None:
        """
        """
        self.n = num_sides
        self.s = side_length

    def __repr__(self):
        return f"Polygon with {self.n} sides of length {self.s}"

    def perimeter(self) -> float:
        """
        Return the perimeter of the polygon.
        """
        return self.n * self.s

    def interior_angle(self):
        """
        Return the measure of each interior angle of the polygon (in degrees).
        """
        return (self.n - 2) * 180 / self.n

    def area(self) -> float:
        """
        Return the area of the polygon. Overridden in subclasses.
        """
        raise NotImplementedError

    # def area(self) -> float:
    #     """Return the area of the regular polygon."""
    #     return (0.25 * self.n * self.s ** 2) / math.tan(math.pi / self.n)

    def num_sides(self) -> int:
        """
        Return the number of sides in the polygon.
        """
        return self.n

    def side_length(self) -> float:
        """
        Return the length of a side of the polygon.
        """
        return self.s

    def scale(self, factor):
        """
        Scale the polygon by a factor.
        """
        self.s *= factor

    def name(self) -> str:
        """
        Return the name of the polygon.
        """
        if self.n == 3:
            return "Triangle"
        elif self.n == 4:
            return "Quadrilateral"
        elif self.n == 5:
            return "Pentagon"
        elif self.n == 6:
            return "Hexagon"
        elif self.n == 7:
            return "Heptagon"
        elif self.n == 8:
            return "Octagon"
        else:
            return f"{self.n}-gon"

    def apothem(self) -> float:
        """
        Return the length of the apothem of the polygon.
        """
        return self.s / (2 * math.tan(math.pi / self.n))

    def is_regular(self) -> bool:
        """
        Return whether the polygon is regular (all sides and angles are equal).
        """
        return True  # By default, the polygons we're dealing with are regular.

    def exterior_angle(self):
        """
        Return the measure of each exterior angle of the polygon (in degrees).
        """
        return 360 / self.n

    def circumradius(self):
        """
        Return the circumradius of the polygon.
        """
        return self.s / (2 * math.sin(math.pi / self.n))

    def centroid(self):
        """
        Return the centroid of the polygon. For regular polygons,
        this is also the center of the circumcircle.
        """
        return (0, 0)  # For a regular polygon, the centroid is at the origin.

    def is_similar(self, other):
        """
        Return whether this polygon is similar to another polygon.
        """
        return self.n == other.n

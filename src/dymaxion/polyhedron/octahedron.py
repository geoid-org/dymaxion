# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Octahedron Class
=========================
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
from ..utils.math import phi


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Octahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Octahedron:
    """
    Octahedron Class

    Regular unit Octahedron.
    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method

        Vertex coordinates:
        (±1,  0,  0)
        ( 0, ±1,  0)
        ( 0,  0, ±1)

        """
        vertices = [
            [-1, 0, 0],
            [1, 0, 0],
            [0, -1, 0],
            [0, 1, 0],
            [0, 0, -1],
            [0, 0, 1],
        ]
        return vertices

    @staticmethod
    def calc_area_from_edge_length(a: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Octahedron.

        Parameters:
            edge_length (float | int): The radius of the Octahedron.

        Returns:
            area (float): The area of the Octahedron.

        """
        area = (2 * math.sqrt(3)) * a * a
        return area

    @staticmethod
    def calc_volume_from_edge_length(a: float | int) -> float:
        """
        Calculate Volume Static Method
        ------------------------------

        Formula to calculate the volume of a Octahedron
        Thus the volume is four times that of a regular tetrahedron with the
        same edge length, while the surface area is twice (because we have
        8 rather than 4 triangles).

        Parameters:
            a (float | int): The edge length of the Octahedron.

        Returns:
            area (float): The area of the Octahedron.

        """
        volume = (1 / 3) * math.sqrt(2) * (a * a * a)
        return volume

    @staticmethod
    def calc_radius_circumsphere(a) -> float:
        """
        Radius of circumsphere
        If the edge length of a regular octahedron is a, the radius of a
        circumscribed sphere (one that touches the octahedron at all vertices).

        ~ 0.707 * a

        """
        radius = (math.sqrt(2) / 2) * a
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces
        the radius of an inscribed sphere (tangent to each of the octahedron's
        faces)

        ~ 0.408 * a

        """
        radius = (math.sqrt(6) / 6) * a
        return radius

    @staticmethod
    def calc_radius_midsphere(a) -> float:
        """
        Radius of midsphere that is tangent to edges

        while the midradius, which touches the middle of each edge, is

        """
        # radius = (1 / 2) * a
        # radius = 0.5 * a
        radius = a / 2
        return radius

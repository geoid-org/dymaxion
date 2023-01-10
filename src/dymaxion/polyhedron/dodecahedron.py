# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Dodecahedron Class
===================
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

__all__ = ["Dodecahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Dodecahedron:
    """
    Dodecahedron Class

    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method

        The following Cartesian coordinates define the 20 vertices of a regular
        dodecahedron centered at the origin and suitably scaled and oriented:

        Vertex coordinates:
        (  ±1,   ±1,   ±1)
        (   0,   ±ϕ, ±1/ϕ)
        (±1/ϕ,    0,   ±ϕ)
        (  ±ϕ, ±1/ϕ,    0)

        """
        vertices = [
            [-1, -1, -1],
            [-1, -1, 1],
            [-1, 1, -1],
            [-1, 1, 1],
            [1, -1, -1],
            [1, -1, 1],
            [1, 1, -1],
            [1, 1, 1],
            [0, -phi, -(1 / phi)],
            [0, -phi, (1 / phi)],
            [0, phi, -(1 / phi)],
            [0, phi, (1 / phi)],
            [-phi, 0, -(1 / phi)],
            [-phi, 0, (1 / phi)],
            [phi, 0, -(1 / phi)],
            [phi, 0, (1 / phi)],
            [-phi, -(1 / phi), 0],
            [-phi, (1 / phi), 0],
            [phi, -(1 / phi), 0],
            [phi, (1 / phi), 0],
        ]
        return vertices

    @staticmethod
    def calc_area_from_edge_length(a: float | int) -> float:
        """

        Formula to calculate area of Dodecahedron

        ~ 20.645728807 * a * a

        """
        area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a * a
        return area

    @staticmethod
    def calc_volume_from_edge_length(a: float | int) -> float:
        """

        Formula to calculate volume of Dodecahedron
        """
        volume = 0.25 * (15 + 7 * math.sqrt(5)) * a * a * a
        # volume = (1 / 4) * (15 + 7 * math.sqrt(5)) * a * a * a
        return volume

    @staticmethod
    def calc_radius_circumsphere(a) -> float:
        """
        Radius of circumsphere
        the radius of a circumscribed sphere (one that touches the Dodecahedron
        at all vertices)

        ~ 1.401258538 * a

        """
        radius = a * (math.sqrt(3) / 4) * (1 + math.sqrt(5))
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces
        The radius of an inscribed sphere (tangent to each of the
        Dodecahedron's faces) is

        ~ 1.113516364 * a

        """
        radius = a * 0.5 * math.sqrt(2.5 + 1.1 * math.sqrt(5))
        # radius = a * (1 / 2) * math.sqrt((5 / 2) + (11 / 10) * math.sqrt(5))
        return radius

    @staticmethod
    def calc_radius_midsphere(a) -> float:
        """
        Radius of midsphere that is tangent to edges

        while the midradius, which touches the middle of each edge, is

        ~ 1.309016994 * a

        """
        radius = a * 0.25 * (3 + math.sqrt(5))
        # radius = a * (1 / 4) * (3 + math.sqrt(5))
        return radius

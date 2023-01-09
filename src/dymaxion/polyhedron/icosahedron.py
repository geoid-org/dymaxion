# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Icosahedron Class
==========================
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

__all__ = ["Icosahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Icosahedron:
    """
    Icosahedron Class
    =================

    Regular unit icosahedron.
    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        12 principal directions in 3D space: points on an unit Icosahedron.

        Vertex coordinates:
        ( 0, ±1, ±φ)
        (±1, ±φ,  0)
        (±φ,  0, ±1)
        or:
        ( 0, ±φ, ±1)
        (±φ, ±1,  0)
        (±1,  0, ±φ)

        """
        vertices = [
            [0, phi, 1],
            [0, phi, -1],
            [0, -phi, 1],
            [0, -phi, -1],
            [1, 0, phi],
            [1, 0, -phi],
            [-1, 0, phi],
            [-1, 0, -phi],
            [phi, 1, 0],
            [phi, -1, 0],
            [-phi, 1, 0],
            [-phi, -1, 0],
        ]
        return vertices

    @staticmethod
    def faces() -> List[Num]:
        """
        20 faces
        """
        faces = [
            [0, 5, 1], [0, 3, 5], [0, 2, 3], [0, 4, 2], [0, 1, 4],
            [1, 5, 8], [5, 3, 10], [3, 2, 7], [2, 4, 11], [4, 1, 9],
            [7, 11, 6], [11, 9, 6], [9, 8, 6], [8, 10, 6], [10, 7, 6],
            [2, 11, 7], [4, 9, 11], [1, 8, 9], [5, 10, 8], [3, 7, 10],
        ]
        return faces

    @staticmethod
    def calc_area_from_edge_length(a: float | int) -> float:
        """

        Formula to calculate area of Icosahedron
        """
        area = 5 * math.sqrt(3) * a * a
        return area

    @staticmethod
    def calc_volume_from_edge_length(a: float | int) -> float:
        """

        Formula to calculate volume of Icosahedron
        """
        volume = ((5 / 12) * (3 + math.sqrt(5)) * a * a * a)
        return volume

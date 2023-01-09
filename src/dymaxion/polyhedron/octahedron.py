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


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Octahedron", ]


# =============================================================================
# Classes
# =============================================================================

class Octahedron:
    """
    Octahedron Class

    Regular unit Octahedron.
    """

    @staticmethod
    def vertices() -> list:
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
    def faces() -> list:
        """
        Faces Static Method

        Returns:
            faces (list): The return value.

        """
        faces = [
        ]
        return faces

    @staticmethod
    def calc_area(r: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Octahedron

        Parameters:
            r (float | int): The radius of the Octahedron.

        Returns:
            area (float): The area of the Octahedron.

        """
        # area = float(6 * r * r)
        # return area
        pass

    @staticmethod
    def calc_volume(r: float | int) -> float:
        """
        Calculate Volume Static Method
        ----------------------------

        Formula to calculate the volume of a Octahedron

        Args:
            r (float | int): The radius of the Octahedron.

        Returns:
            area (float): The area of the Octahedron.

        """
        volume = float(r * r * r)
        return volume

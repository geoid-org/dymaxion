# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Tetrahedron Class
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


# =============================================================================
# Variables
# =============================================================================

__all__ = [" Tetrahedron", ]


# =============================================================================
# Classes
# =============================================================================

class Tetrahedron:
    """
     Tetrahedron Class

    Regular unit cube.
    """

    @staticmethod
    def vertices() -> list:
        """
        Vertices Static Method

        Vertex coordinates:
        ( 1,  1,  1)
        ( 1, -1, -1)
        (-1,  1, -1)
        (-1, -1,  1)
        or:
        (-1, -1, -1)
        (-1,  1,  1)
        ( 1, -1,  1)
        ( 1,  1, -1)

        """
        vertices = [
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
        ]
        return vertices

    @staticmethod
    def faces() -> list:
        """
        Faces Static Method

        Returns:
            faces (list): The return value. True for success, False otherwise.

        """
        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 4, 5],
            [2, 3, 6, 7],
            [0, 3, 4, 7],
            [1, 2, 5, 6],
        ]
        return faces

    @staticmethod
    def calc_area(r: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a  Tetrahedron

        Parameters:
            r (float | int): The radius of the Tetrahedron.

        Returns:
            area (float): The area of the Tetrahedron.

        """
        area = float(6 * r * r)
        return area

    @staticmethod
    def calc_volume(r: float | int) -> float:
        """
        Calculate Volume Static Method
        ----------------------------

        Formula to calculate the volume of a  Tetrahedron

        Args:
            r (float | int): The radius of the Tetrahedron.

        Returns:
            area (float): The area of the Tetrahedron.

        """
        volume = float(r * r * r)
        return volume

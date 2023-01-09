# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Cube Class
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

__all__ = ["Cube", ]


# =============================================================================
# Classes
# =============================================================================

class Cube:
    """
    Cube Class

    Regular unit cube.
    """

    @staticmethod
    def vertices() -> list:
        """
        Vertices Static Method

        Vertex coordinates:
        (±1, ±1, ±1)

        Returns:
            vertices (list): The vertex coordinates of the Cube.
        """
        vertices = [
            [-1, -1, -1],
            [-1, -1, 1],
            [-1, 1, 1],
            [-1, 1, -1],
            [1, -1, -1],
            [1, -1, 1],
            [1, 1, 1],
            [1, 1, -1],
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
    def calc_area(radius: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Cube

        Parameters:
            radius (float | int): The radius of the Cube.

        Returns:
            area (float): The area of the Cube.

        """
        area = float(6 * radius * radius)
        return area

    @staticmethod
    def calc_volume(radius: float | int) -> float:
        """
        Calculate Volume Static Method
        ----------------------------

        Formula to calculate the volume of a Cube

        Args:
            radius (float | int): The radius of the Cube.

        Returns:
            area (float): The area of the Cube.

        """
        volume = float(radius * radius * radius)
        return volume

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
from ..utils.math import phi


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Tetrahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Tetrahedron:
    """
    Tetrahedron Class

    Regular unit cube.
    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method

        Vertex coordinates:

        ( 1,  1,  1)\
        ( 1, -1, -1)\
        (-1,  1, -1)\
        (-1, -1,  1)\

        or:

        (-1, -1, -1)\
        (-1,  1,  1)\
        ( 1, -1,  1)\
        ( 1,  1, -1)\

        """
        vertices = [
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
        ]
        return vertices

    @staticmethod
    def calc_area_from_edge_length(a: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Tetrahedron.

        Parameters:
            edge_length (float | int): The radius of the Tetrahedron.

        Returns:
            area (float): The area of the Tetrahedron.

        """
        # area = 4 * Tetrahedron.calc_face_area(a)
        area = math.sqrt(3) * a * a
        return area

    @staticmethod
    def calc_volume_from_edge_length(a: float | int) -> float:
        """
        Calculate Volume Static Method
        ------------------------------

        Formula to calculate the volume of a Tetrahedron

        Parameters:
            a (float | int): The edge length of the Tetrahedron.

        Returns:
            area (float): The area of the Tetrahedron.

        """
        # volume = (1 / 3) * Tetrahedron.calc_face_area(a) * Tetrahedron.calc_pyramid_height(a)  # noqa E501
        volume = (math.sqrt(2) / 12) * (a * a * a)
        # volume = (a * a * a) / (6 * math.sqrt(2))
        return volume

    @staticmethod
    def calc_face_area(a) -> float:
        """

        """
        face_area = math.sqrt(3 / 4) * a * a
        return face_area

    @staticmethod
    def calc_pyramid_height(a) -> float:
        """
        Height of pyramid

        """
        # height = (math.sqrt(6) / 3) * a
        height = math.sqrt(2 / 3) * a
        return height

    @staticmethod
    def calc_distance_centroid_vertex(a) -> float:
        """
        Centroid to vertex distance

        """
        # distance = 3 * Tetrahedron.calc_pyramid_height(a)
        # distance = (math.sqrt(6) / 4) * a
        distance = math.sqrt(3 / 8) * a
        return distance

    @staticmethod
    def calc_distance_edge_edge(a) -> float:
        """
        Edge to opposite edge distance

        """
        distance = (1 / math.sqrt(2)) * a
        return distance

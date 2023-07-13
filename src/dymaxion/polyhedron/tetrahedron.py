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
from ..utils.constants import (phi, ksi)
from ._polyhedron import Polyhedron

# =============================================================================
# Variables
# =============================================================================

__all__ = ["Tetrahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Tetrahedron(Polyhedron):
    """
    Tetrahedron Class
    =================

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
    def calc_area(a: float | int) -> float:
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
    def calc_volume(a: float | int) -> float:
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
        # face_area = a * 0.25 * math.sqrt(3)
        # # face_area = a * (1 / 4) * math.sqrt(3)
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

    @staticmethod
    def calc_angle_face_vertex_edge(a) -> float:
        """
        Face-vertex-edge angle
        (approx. 54.7356°)

        """
        # angle = math.acos(1 / math.sqrt(3))
        angle = math.atan(math.sqrt(2))
        return angle

    @staticmethod
    def calc_angle_dihedral() -> float:
        """
        Face-edge-face angle, i.e., "dihedral angle"
        (approx. 70.5288°)

        """
        angle = math.acos(1 / 3)
        # angle = math.atan(2 * math.sqrt(2))
        return angle

    @staticmethod
    def calc_angle_subtended() -> float:
        """
        Vertex-Center-Vertex angle
        calc_face_angle_face_edge_face
        The angle between lines from the tetrahedron center to any two
        vertices. It is also the angle between Plateau borders at a vertex.
        In chemistry it is called the tetrahedral bond angle. This angle
        (in radians) is also the length of the circular arc on the unit sphere
        resulting from centrally projecting one edge of the tetrahedron to the
        sphere.

        (approx. 109.4712°)

        """
        angle = math.acos(-1 / 3)
        # angle = 2 * math.atan(math.sqrt(2))
        return angle

    @staticmethod
    def calc_angle_solid_vertex() -> float:
        """
        Solid angle at a vertex subtended by a face
        (approx. 0.55129 steradians)
        (approx. 1809.8 square degrees)

        """
        angle = math.acos(23 / 27)
        return angle

    @staticmethod
    def calc_angle_solid_face() -> float:
        """

        """
        angle = math.pi
        return angle

    @staticmethod
    def calc_radius_circumsphere(a) -> float:
        """
        Radius of circumsphere

        0.61237
        """
        # radius = (math.sqrt(6) / 4) * a
        radius = math.sqrt(3 / 8) * a
        radius = a * 0.25 * math.sqrt(6)
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces

        0.20412

        """
        radius = a * (1 / 12) * math.sqrt(6)
        # radius = (1 / 3) * Tetrahedron.calc_radius_circumsphere(a)
        radius = a / math.sqrt(24)
        return radius

    @staticmethod
    def calc_radius_midsphere(a) -> float:
        """
        Radius of midsphere that is tangent to edges

        0.35355

        """
        # radius = math.sqrt(Tetrahedron.calc_radius_circumsphere(a) * Tetrahedron.calc_radius_insphere(a))  # noqa E501
        radius = a * 0.25 * math.sqrt(2)
        # radius = a * (1 / 4) * math.sqrt(2)
        # radius = a / math.sqrt(8)
        return radius

    @staticmethod
    def calc_radius_exsphere(a) -> float:
        """
        Radius of exspheres

        """
        radius = a / math.sqrt(6)
        return radius

    @staticmethod
    def calc_distance_exsphere_vertex(a) -> float:
        """
        Distance to exsphere center from the opposite vertex

        """
        # distance = (math.sqrt(6) / 2) * a
        distance = math.sqrt(3 / 2) * a
        return distance

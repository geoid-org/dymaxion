# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Hexahedron Class
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
from ..utils.constants import (phi, ksi)
from ._polyhedron import Polyhedron


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Hexahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Hexahedron(Polyhedron):
    """
    Hexahedron Class
    ================

    Regular unit cube.

    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method

        Vertex coordinates:
        (±1, ±1, ±1)

        Returns:
            vertices (list): The vertex coordinates of the Hexahedron.
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
    def get_unit_faces() -> List[Num]:
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
    def calc_area(a: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Hexahedron

        Parameters:
            edge_length (float | int): The radius of the Hexahedron.

        Returns:
            area (float): The area of the Hexahedron.

        """
        area = float(6 * a * a)
        return area

    @staticmethod
    def calc_volume(a: float | int) -> float:
        """
        Calculate Volume Static Method
        ------------------------------

        Formula to calculate the volume of a Hexahedron

        Parameters:
            a (float | int): The edge length of the Hexahedron.

        Returns:
            area (float): The area of the Hexahedron.

        """
        volume = float(a * a * a)
        return volume

    @staticmethod
    def calc_face_diagonal(a: float | int) -> float:
        """

        """
        face_diagonal = float(math.sqrt(a * a))
        return face_diagonal

    @staticmethod
    def calc_space_diagonal(a: float | int) -> float:
        """

        """
        space_diagonal = float(math.sqrt(a * a * a))
        return space_diagonal

    @staticmethod
    def calc_radius_circumsphere(a: float | int) -> float:
        """
        radius of circumscribed sphere
        """
        radius = a * 0.5 * math.sqrt(3)
        # radius = a * (1 / 2) * math.sqrt(3)
        # radius = (math.sqrt(3) / 2) * a
        return radius

    @staticmethod
    def calc_radius_insphere(a: float | int) -> float:
        """
        radius of inscribed sphere
        """
        radius = float(a / 2)
        return radius

    @staticmethod
    def calc_radius_midsphere(a: float | int) -> float:
        """
        radius of sphere tangent to edges
        """
        radius = a * 0.5 * math.sqrt(2)
        # radius = a / math.sqrt(2)
        return radius

    @staticmethod
    def calc_face_angles() -> float:
        """
        angles between faces (in radians)
        """
        face_angles = phi / 2
        return face_angles

    @staticmethod
    def calc_angle_solid_face() -> float:
        """

        """
        angle = (2 * math.pi) / 3
        return angle

    @staticmethod
    def calc_angle_solid_vertex() -> float:
        """
        Solid angle at a vertex subtended by a face
        (approx. 1.57080 steradians)

        """
        angle = math.pi / 2
        return angle

    @staticmethod
    def calc_angle_dihedral(a) -> float:
        """
        Face-edge-face angle, i.e., "dihedral angle"
        (approx. 90.0000)

        """
        angle = math.pi / 2
        return angle

    @staticmethod
    def calc_angle_subtended(a) -> float:
        """
        Vertex-Center-Vertex angle
        calc_face_angle_face_edge_face
        The angle between lines from the hexaahedron center to any two
        vertices. It is also the angle between Plateau borders at a vertex.
        In chemistry it is called the tetrahedral bond angle. This angle
        (in radians) is also the length of the circular arc on the unit sphere
        resulting from centrally projecting one edge of the hexaahedron to the
        sphere.

        (approx. 70.529°)

        """
        angle = math.acos(1 / 3)
        return angle

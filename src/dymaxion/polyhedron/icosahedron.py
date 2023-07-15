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
from ..utils.constants import (phi, ksi)
from ._polyhedron import Polyhedron


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Icosahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Icosahedron(Polyhedron):
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

        Position 1
        ( 0, ±1, ±φ)
        (±1, ±φ,  0)
        (±φ,  0, ±1)

        or:

        Position 2
        ( 0, ±φ, ±1)
        (±φ, ±1,  0)
        (±1,  0, ±φ)

        """

        vertices = [
            [0, -1, -phi],
            [0, -1, phi],
            [0, 1, -phi],
            [0, 1, phi],
            [-1, -phi, 0],
            [-1, phi, 0],
            [1, -phi, 0],
            [1, phi, 0],
            [-phi, 0, -1],
            [-phi, 0, 1],
            [phi, 0, -1],
            [phi, 0, 1],
        ]
        # vertices = [ # other config
        #     [0, phi, 1],
        #     [0, phi, -1],
        #     [0, -phi, 1],
        #     [0, -phi, -1],
        #     [1, 0, phi],
        #     [1, 0, -phi],
        #     [-1, 0, phi],
        #     [-1, 0, -phi],
        #     [phi, 1, 0],
        #     [phi, -1, 0],
        #     [-phi, 1, 0],
        #     [-phi, -1, 0],
        # ]
        return vertices

    @staticmethod
    def faces() -> List[Num]:
        """
        20 faces
        """
        faces = [

        ]
        # faces = [# other config
        #     [0, 5, 1], [0, 3, 5], [0, 2, 3], [0, 4, 2], [0, 1, 4],
        #     [1, 5, 8], [5, 3, 10], [3, 2, 7], [2, 4, 11], [4, 1, 9],
        #     [7, 11, 6], [11, 9, 6], [9, 8, 6], [8, 10, 6], [10, 7, 6],
        #     [2, 11, 7], [4, 9, 11], [1, 8, 9], [5, 10, 8], [3, 7, 10],
        # ]
        return faces

    @staticmethod
    def calc_area(a: float | int) -> float:
        """

        Formula to calculate area of Icosahedron
        """
        area = 5 * math.sqrt(3) * a * a
        return area

    @staticmethod
    def calc_volume(a: float | int) -> float:
        """

        Formula to calculate volume of Icosahedron
        """
        volume = ((5 / 12) * (3 + math.sqrt(5)) * a * a * a)
        return volume

    @staticmethod
    def calc_radius_circumsphere(a) -> float:
        """
        Radius of circumsphere
        the radius of a circumscribed sphere (one that touches the icosahedron
        at all vertices)

        ~ 0.9510565163 * a

        """
        # radius = (a / 2) * math.sqrt(phi * math.sqrt(5))
        radius = (a / 4) * math.sqrt(10 + 2 * math.sqrt(5))
        # radius = a * math.sin((2* phi) / 5)
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces
        The radius of an inscribed sphere (tangent to each of the 
        icosahedron's faces) is

        ~ 0.7557613141 * a

        """
        # radius = a * (1 / 12) * (3 * math.sqrt(3) + math.sqrt(15))
        # radius = (phi * phi * a) / (2 * math.sqrt(3))
        radius = a * (math.sqrt(3) / 12) * (3 + math.sqrt(5))
        return radius

    @staticmethod
    def calc_radius_midsphere(a) -> float:
        """
        Radius of midsphere that is tangent to edges

        while the midradius, which touches the middle of each edge, is

        """
        radius = (a * phi) / 2
        # radius = (1 / 4) * (1 + math.sqrt(5)) * a
        # radius = 0.25 * (1 + math.sqrt(5)) * a
        # radius = a * math.cos(phi / 5)
        return radius

    @staticmethod
    def calc_angle_solid_vertex() -> float:
        """
        Solid angle at a vertex subtended by a face
        (approx. 2.63455 steradians)

        """
        angle = 2 * math.pi - 5 * math.asin(2 / 3)
        return angle

    @staticmethod
    def calc_angle_solid_face() -> float:
        """

        """
        angle = math.pi / 5
        return angle

    @staticmethod
    def calc_angle_dihedral() -> float:
        """
        Face-edge-face angle, i.e., "dihedral angle"
        (approx. 138.190)

        """
        angle = math.acos((-1 / 3) * math.sqrt(5))
        return angle

    @staticmethod
    def calc_angle_subtended(a) -> float:
        """
        Vertex-Center-Vertex angle
        calc_face_angle_face_edge_face
        The angle between lines from the dodecahedron center to any two
        vertices. It is also the angle between Plateau borders at a vertex.
        In chemistry it is called the tetrahedral bond angle. This angle
        (in radians) is also the length of the circular arc on the unit sphere
        resulting from centrally projecting one edge of the dodecahedron to the
        sphere.

        (approx. 63.435)

        """
        angle = math.acos((1 / 5) * math.sqrt(5))
        return angle




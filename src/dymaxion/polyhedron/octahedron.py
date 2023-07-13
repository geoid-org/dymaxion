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
from ..utils.constants import (phi, ksi)
from ._polyhedron import Polyhedron


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Octahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Octahedron(Polyhedron):
    """
    Octahedron Class
    ================

    Regular unit Octahedron.

    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method
        ----------------------

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
    def calc_area(a: float | int) -> float:
        """
        Calculate Area Static Method
        ----------------------------

        Formula to calculate the area of a Octahedron.

        Parameters:
            edge_length (float | int): The radius of the Octahedron.

        Returns:
            area (float): The area of the Octahedron.

        """
        area = 2 * math.sqrt(3) * a * a
        return area

    @staticmethod
    def calc_volume(a: float | int) -> float:
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
        radius = a * 0.5 * math.sqrt(2)
        # radius = a * (math.sqrt(2) / 2)
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces
        the radius of an inscribed sphere (tangent to each of the octahedron's
        faces)

        ~ 0.408 * a

        """
        # radius = (math.sqrt(6) / 6) * a
        # radius = a * (1 / 6) * math.sqrt(6)
        radius = (math.sqrt(6) * a) / 6
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

    @staticmethod
    def calc_angle_solid_vertex() -> float:
        """
        Solid angle at a vertex subtended by a face
        (approx. 1.35935 steradians)

        """
        angle = 4 * math.asin(1 / 3)
        return angle

    @staticmethod
    def calc_angle_dihedral() -> float:
        """
        Face-edge-face angle, i.e., "dihedral angle"
        (approx. 109.471)

        """
        angle = math.acos(-1 / 3)
        return angle

    @staticmethod
    def calc_angle_subtended() -> float:
        """
        angles beta subtended by an edge from the center for the Platonic
        solids (Cundy and Rollett 1989, Table II following p. 144).
        Vertex-Center-Vertex angle
        calc_face_angle_face_edge_face
        The angle between lines from the dodecahedron center to any two
        vertices. It is also the angle between Plateau borders at a vertex.
        In chemistry it is called the tetrahedral bond angle. This angle
        (in radians) is also the length of the circular arc on the unit sphere
        resulting from centrally projecting one edge of the dodecahedron to the
        sphere.

        (approx. 90.000)

        """
        angle = math.pi / 2
        return angle

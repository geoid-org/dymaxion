# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Dodecahedron Class
===========================
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

__all__ = ["Dodecahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Dodecahedron(Polyhedron):
    """
    Dodecahedron Class
    ==================

    """

    @staticmethod
    def vertices() -> List[Num]:
        """
        Vertices Static Method

        The following Cartesian coordinates define the 20 vertices of a regular
        dodecahedron centered at the origin and suitably scaled and oriented:

        Vertex coordinates:

        Position 1
        (  ±1,   ±1,   ±1)
        (   0, ±1/ϕ,   ±ϕ)
        (±1/ϕ,   ±ϕ,    0)
        (  ±ϕ,    0, ±1/ϕ)

        or:

        Position 2
        (  ±1,   ±1,   ±1)
        (   0,   ±ϕ, ±1/ϕ)
        (  ±ϕ, ±1/ϕ,    0)
        (±1/ϕ,    0,   ±ϕ)

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
            [0, -(1 / phi), -phi],
            [0, -(1 / phi), phi],
            [0, (1 / phi), -phi],
            [0, (1 / phi), phi],
            [-(1 / phi), -phi, 0],
            [-(1 / phi), phi, 0],
            [(1 / phi), -phi, 0],
            [(1 / phi), phi, 0],
            [-phi, 0, -(1 / phi)],
            [-phi, 0, (1 / phi)],
            [phi, 0, -(1 / phi)],
            [phi, 0, (1 / phi)],
        ]
        # vertices = [ # Position 2
        #     [-1, -1, -1],
        #     [-1, -1, 1],
        #     [-1, 1, -1],
        #     [-1, 1, 1],
        #     [1, -1, -1],
        #     [1, -1, 1],
        #     [1, 1, -1],
        #     [1, 1, 1],
        #     [0, -phi, -(1 / phi)],
        #     [0, -phi, (1 / phi)],
        #     [0, phi, -(1 / phi)],
        #     [0, phi, (1 / phi)],
        #     [-phi, -(1 / phi), 0],
        #     [-phi, (1 / phi), 0],
        #     [phi, -(1 / phi), 0],
        #     [phi, (1 / phi), 0],
        #     [-phi, 0, -(1 / phi)],
        #     [-phi, 0, (1 / phi)],
        #     [phi, 0, -(1 / phi)],
        #     [phi, 0, (1 / phi)],
        # ]
        return vertices

    @staticmethod
    def calc_area(a: float | int) -> float:
        """

        Formula to calculate area of Dodecahedron

        ~ 20.645728807 * a * a

        """
        area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a * a
        return area

    @staticmethod
    def calc_volume(a: float | int) -> float:
        """

        Formula to calculate volume of Dodecahedron
        """
        _ = 0.25 * (15 + 7 * math.sqrt(5)) * a * a * a
        # _ = ((15 + 7 * math.sqrt(5)) * a * a * a) / 4
        # _ = (1 / 4) * (15 + 7 * math.sqrt(5)) * a * a * a
        return _

    @staticmethod
    def calc_radius_circumsphere(a) -> float:
        """
        Radius of circumsphere
        the radius of a circumscribed sphere (one that touches the Dodecahedron
        at all vertices)

        ~ 1.401258538 * a

        """
        radius = a * 0.25 * (math.sqrt(15) + math.sqrt(3))
        # radius = a * (1 / 4) * (math.sqrt(15) + math.sqrt(3))
        # radius = a * (math.sqrt(3) / 4) * (1 + math.sqrt(5))
        return radius

    @staticmethod
    def calc_radius_insphere(a) -> float:
        """
        Radius of insphere that is tangent to faces
        The radius of an inscribed sphere (tangent to each of the
        Dodecahedron's faces) is

        ~ 1.113516364 * a

        """
        radius = a * 0.05 * math.sqrt(250 + 110 * math.sqrt(5))
        # radius = a * (1 / 20) * math.sqrt(250 + 110 * math.sqrt(5))
        # radius = a * 0.5 * math.sqrt(2.5 + 1.1 * math.sqrt(5))
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

    @staticmethod
    def calc_angle_solid_vertex() -> float:
        """
        Solid angle at a vertex subtended by a face
        (approx. 2.96174 steradians)

        """
        angle = math.pi - math.atan(2 / 11)
        return angle

    @staticmethod
    def calc_angle_solid_face() -> float:
        """

        """
        angle = math.pi / 3
        return angle

    @staticmethod
    def calc_angle_dihedral() -> float:
        """
        Face-edge-face angle, i.e., "dihedral angle"
        (approx. 116.565)

        """
        angle = math.acos((-1 / 5) * math.sqrt(5))
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

        (approx. 41.810)

        """
        angle = math.acos((1 / 3) * math.sqrt(5))
        return angle

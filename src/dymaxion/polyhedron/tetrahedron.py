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
    def calc_face_area(a) -> float:
        """

        """
        face_area = math.sqrt(3 / 4) * a * a
        return face_area



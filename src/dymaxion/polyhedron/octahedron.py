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
from ..utils.math import phi


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Octahedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Octahedron:
    """
    Octahedron Class

    Regular unit Octahedron.
    """

    @staticmethod
    def vertices() -> List[Num]:
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

# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Polyhedron Class
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


# =============================================================================
# Variables
# =============================================================================

__all__ = ["Polyhedron", ]

Num = Union[int, float]


# =============================================================================
# Classes
# =============================================================================

class Polyhedron(object):
    """
    Polyhedron Class

    """

    def __init__(self):
        self.name = ""

    # @abstractmethod
    # def get_name(self):
    #     return self.name

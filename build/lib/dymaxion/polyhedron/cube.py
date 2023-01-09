import math


class Cube:
    """
    Cube Class
    ==========

    Regular unit cube.
    """

    @staticmethod
    def vertices() -> list:
        """
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
    def calc_area(r: float | int) -> float:
        """

        Formula to calculate area of Cube
        """
        area = 6 * r * r
        return area

    @staticmethod
    def calc_volume(r: float | int) -> float:
        """

        Formula to calculate volume of Cube
        """
        volume = r * r * r
        return volume

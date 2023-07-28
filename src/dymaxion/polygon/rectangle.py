from ._polygon import Polygon

import math

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4, None)
        self._length = length
        self._width = width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * self._length + 2 * self._width

    def area(self):
        """Return the area of the rectangle."""
        return self._length * self._width

    def diagonal(self):
        """Return the length of the diagonal of the rectangle."""
        return math.sqrt(self._length**2 + self._width**2)

    def get_length(self):
        """Return the length of the rectangle."""
        return self._length

    def get_width(self):
        """Return the width of the rectangle."""
        return self._width

    def set_length(self, length):
        """Set the length of the rectangle."""
        if length > 0:
            self._length = length
        else:
            raise ValueError("Length must be a positive number")

    def set_width(self, width):
        """Set the width of the rectangle."""
        if width > 0:
            self._width = width
        else:
            raise ValueError("Width must be a positive number")

    def is_square(self):
        """Check if the rectangle is a square."""
        return self._length == self._width

    def __repr__(self):
        shape = "Square" if self.is_square() else "Rectangle"
        return f"{shape} with length {self._length} and width {self._width}"


# class rectangle(Polygon):

#     def __init__(self,breadth,length):
#         Polygon.__init__(self, 4)
#         self.breadth = breadth
#         self.length = length

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

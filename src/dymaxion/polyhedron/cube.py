
class Cube:
    def __init__(self, r):
        self.radius = radius
        self.surfaceArea = 0
        self.volume = 0
    
    def getRadius(self):
        r = self.radius
        self.area = 6 * r * r
        return (self.area)
    
    def getVolume(self):
        r = self.radius
        self.volume = r * r * r
        return (self.volume)

class Cube:

    def __init__(self, nbrsides):
        self.nbr_sides = nbrsides

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

    edges = select_shortest_edges(vertices)

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

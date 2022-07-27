import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self._x - x), abs(self._y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self._vertice1 = vertice1
        self._vertice2 = vertice2
        self._vertice3 = vertice3

    def perimeter(self):
        return math.hypot(abs)
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

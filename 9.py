import math


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def display_area(shape):
    print("Area:", shape.area())


rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(10, 6)

display_area(rectangle)
display_area(circle)
display_area(triangle)
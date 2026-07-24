
# ---------------------------------------------------------
# Problem 12.1 - The Triangle Class
# CS2030 - Assignment 3
# ---------------------------------------------------------

import math

class GeometricObject:
    def __init__(self, color="white", filled=False):
        self.color = color
        self.filled = filled


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="white", filled=False):
        super().__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Accessors
    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    # Perimeter
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    # Area using Heron's formula
    def getArea(self):
        s = self.getPerimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    # String description
    def __str__(self):
        return f"Triangle: side1={self.side1}, side2={self.side2}, side3={self.side3}"


# ------------------ TEST PROGRAM -------------------------
if __name__ == "__main__":
    t = Triangle(3, 4, 5, "blue", True)
    print(t)
    print("Area:", t.getArea())
    print("Perimeter:", t.getPerimeter())

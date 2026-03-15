import math

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a, self.b, self.h = a, b, h
    def perimeter(self):
        return 2 * (self.a * self.b)
    def area(self):
        return self.a * self.h


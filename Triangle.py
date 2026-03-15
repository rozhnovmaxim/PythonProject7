import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
def perimeter(self):
    return self.a + self.b + self.c
def area(self):
    p = self.perimeter() / 2
    return math.sqrt(p*(self.a) * (p - self.b) * (p - self.c))



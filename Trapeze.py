import math

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        if self.a == self.b: return 0
        return ((self.a + self.b) / 4 * abs(self.a - self.b)) * \
            math.sqrt((self.a + self.c + self.d - self.b) * (self.b + self.c + self.d - self.a) * (
                        self.a + self.c - self.b - self.d) * (self.a + self.d - self.b - self.c))

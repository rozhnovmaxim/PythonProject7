import math

class Figure:
    def dimention(self): return 2
    def perimetr(self): return None
    def square(self): return None
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None
    def volume(self): return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimetr(self): return self.a + self.b + self.c
    def square(self):
        p = self.perimetr() / 2
        # Перевірка на "можливість" трикутника
        val = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(max(0, val)) # max(0, val) прибирає мінус
    def volume(self): return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def perimetr(self): return 2 * (self.a + self.b)
    def square(self): return self.a * self.b
    def volume(self): return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def perimetr(self): return self.a + self.b + self.c + self.d
    def height(self):
        diff = abs(self.a - self.b)
        if diff == 0: return self.c
        s = (self.c + self.d + diff) / 2
        val = s * (s - self.c) * (s - self.d) * (s - diff)
        return (2 / diff) * math.sqrt(max(0, val))
    def square(self): return ((self.a + self.b) / 2) * self.height()
    def volume(self): return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self._h = a, b, h
    def perimetr(self): return 2 * (self.a + self.b)
    def height(self): return self._h
    def square(self): return self.a * self._h
    def volume(self): return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def perimetr(self): return 2 * math.pi * self.r
    def square(self): return math.pi * self.r**2
    def volume(self): return self.square()

class Ball(Figure):
    def __init__(self, r):
        self.r = r
    def dimention(self): return 3
    def squareSurface(self): return 4 * math.pi * self.r**2
    def volume(self): return (4/3) * math.pi * self.r**3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._h = h
    def dimention(self): return 3
    def height(self): return self._h
    def squareBase(self): return (math.sqrt(3) / 4) * self.a**2
    def volume(self): return (1/3) * self.squareBase() * self._h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._h = h
    def dimention(self): return 3
    def height(self): return self._h
    def squareBase(self): return self.a * self.b
    def volume(self): return (1/3) * self.squareBase() * self._h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimention(self): return 3
    def height(self): return self.c
    def squareBase(self): return self.a * self.b
    def volume(self): return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h
    def dimention(self): return 3
    def height(self): return self._h
    def squareBase(self): return math.pi * self.r**2
    def volume(self): return (1/3) * self.squareBase() * self._h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._h = h
    def dimention(self): return 3
    def height(self): return self._h
    def squareBase(self): return super().square()
    def volume(self): return self.squareBase() * self._h
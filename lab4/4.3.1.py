import turtle
import random

class Figure:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color
        self._t = turtle.Turtle()
        self._t.hideturtle()
        self._t.speed(0)

    def draw(self):
        self._t.pencolor(self._color)
        self._t.fillcolor(self._color)
        self._t.up()
        self._t.goto(self._x, self._y)
        self._t.down()

class Rectangle(Figure):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, color)
        self._w = w
        self._h = h

    def draw(self):
        super().draw()
        self._t.begin_fill()
        for _ in range(2):
            self._t.forward(self._w)
            self._t.left(90)
            self._t.forward(self._h)
            self._t.left(90)
        self._t.end_fill()

class Circle(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r = r

    def draw(self):
        super().draw()
        self._t.begin_fill()
        self._t.circle(self._r)
        self._t.end_fill()

class Triangle(Figure):
    def __init__(self, x, y, s, color):
        super().__init__(x, y, color)
        self._s = s

    def draw(self):
        super().draw()
        self._t.begin_fill()
        for _ in range(3):
            self._t.forward(self._s)
            self._t.left(120)
        self._t.end_fill()

class Stem(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y, 4, 60, "darkgreen")

class Petal(Circle):
    def __init__(self, x, y, color):
        super().__init__(x, y, 10, color)

class Leaf(Triangle):
    def __init__(self, x, y):
        super().__init__(x, y, 15, "darkgreen")

class Flower:
    def __init__(self, x, y, p_color):
        self.stem = Stem(x, y)
        self.leaf = Leaf(x + 2, y + 20)
        self.petals = [
            Petal(x - 8, y + 60, p_color),
            Petal(x + 12, y + 60, p_color),
            Petal(x + 2, y + 75, p_color),
            Petal(x + 2, y + 45, p_color)
        ]

    def draw(self):
        self.stem.draw()
        self.leaf.draw()
        for p in self.petals:
            p.draw()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.tracer(1)
    colors = ["red", "blue", "purple", "yellow", "orange", "pink", "magenta", "cyan"]
    for _ in range(100):
        f = Flower(random.randint(-350, 350), random.randint(-350, 250), random.choice(colors))
        f.draw()
    screen.mainloop()
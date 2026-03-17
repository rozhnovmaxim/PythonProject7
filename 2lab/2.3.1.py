import turtle
import random

class Petal:
    def __init__(self, color):
        self.color = color

    def draw(self, t, x, y, angle):
        t.penup()
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()
        t.pencolor(self.color)
        # Встановлюємо колір заливки пелюстки (червоний-іш)
        t.fillcolor(self.color)

        for _ in range(2):
            t.begin_fill()
            t.circle(40, 60)
            t.left(120)
            t.circle(40, 60)
            t.left(120)
            t.end_fill()

class Leaf:
    def __init__(self, color="#228B22"):
        self.color = color

    def draw(self, t, x, y, angle):
        t.penup()
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        for _ in range(2):
            t.circle(30, 90)
            t.left(90)
        t.end_fill()

class Stem:
    def __init__(self, color="#228B22", length=150):
        self.color = color
        self.length = length

    def draw(self, t, x, y):
        t.penup()
        t.goto(x, y)
        t.setheading(-90)
        t.pendown()
        t.pencolor(self.color)
        t.pensize(4)
        t.forward(self.length)
        t.pensize(1)

class Flower:
    def __init__(self, x, y, petal_color):
        self.x = x
        self.y = y
        self.stem = Stem()
        self.leaf = Leaf()
        self.petal_color = petal_color

    def draw(self, t):
        # Малюємо спочатку стебло та листя (зеленим)
        self.stem.draw(t, self.x, self.y)
        self.leaf.draw(t, self.x, self.y - 60, 30)
        self.leaf.draw(t, self.x, self.y - 100, 150)

        # Потім малюємо 8 зафарбованих пелюсток (червоним) поверх стебла
        for i in range(8):
            p = Petal(self.petal_color)
            p.draw(t, self.x, self.y, i * 45)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    # Змінимо тло на світло-сіре, щоб червоний колір був контрастнішим
    screen.bgcolor("#f0f0f0")
    screen.title("Букет червоних квітів")
    t = turtle.Turtle()
    t.speed(0)

    # Список відтінків червоного для різноманітності
    flower_colors = ['red', '#FF4500', '#DC143C']
    positions = [(-200, 0), (0, 50), (200, -20)]

    for i in range(len(positions)):
        # Створюємо Flower з одним із червоних кольорів
        flower = Flower(positions[i][0], positions[i][1], flower_colors[i])
        flower.draw(t)

    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()
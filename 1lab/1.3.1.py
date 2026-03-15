import math


class Figure:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def __str__(self):
        return f"{self.__class__.__name__}"


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        val = s * (s - self.a) * (s - self.b) * (s - self.c)
        return math.sqrt(val) if val > 0 else 0


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        if self.a == self.b: return 0

        h_sq = self.c ** 2 - (((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.a - self.b))) ** 2
        h = math.sqrt(max(0, h_sq))
        return ((self.a + self.b) / 2) * h


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)


def process_file(filename):
    figures = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.split()
                if not parts: continue

                name = parts[0]
                try:
                    params = [float(p) for p in parts[1:]]
                    if name == "Triangle" and len(params) >= 3:
                        figures.append(Triangle(params[0], params[1], params[2]))
                    elif name == "Rectangle" and len(params) >= 2:
                        figures.append(Rectangle(params[0], params[1]))
                    elif name == "Trapeze" and len(params) >= 4:
                        figures.append(Trapeze(params[0], params[1], params[2], params[3]))
                    elif name == "Parallelogram" and len(params) >= 3:
                        figures.append(Parallelogram(params[0], params[1], params[2]))
                    elif name == "Circle" and len(params) >= 1:
                        figures.append(Circle(params[0]))
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return

    if not figures:
        print("Фігур не знайдено.")
        return

    max_area_fig = max(figures, key=lambda f: f.area())
    max_peri_fig = max(figures, key=lambda f: f.perimeter())

    print(f"Найбільша площа: {max_area_fig} ({max_area_fig.area():.2f})")
    print(f"Найбільший периметр: {max_peri_fig} ({max_peri_fig.perimeter():.2f})")



file_to_read = input("Введіть назву файлу (напр. input03.txt): ")
process_file(file_to_read)
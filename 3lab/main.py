from figures import *


def solve_task(filenames):
    mapping = {
        "Triangle": Triangle, "Rectangle": Rectangle, "Trapeze": Trapeze,
        "Parallelogram": Parallelogram, "Circle": Circle, "Ball": Ball,
        "TriangularPyramid": TriangularPyramid, "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped, "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }

    for filename in filenames:
        max_val = -1
        best_fig = None
        try:
            with open(filename, "r") as f:
                for line in f:
                    data = line.split()
                    if not data: continue
                    name = data[0]
                    params = [float(x) for x in data[1:]]

                    if name in mapping:
                        obj = mapping[name](*params)
                        val = obj.volume()
                        if val is not None and val > max_val:
                            max_val = val
                            best_fig = obj

            if best_fig:
                print(f"Файл: {filename} -> Найбільша міра: {max_val:.2f} ({type(best_fig).__name__})")
        except Exception as e:
            print(f"Помилка у файлі {filename}: {e}")


if __name__ == "__main__":

    solve_task(["input01.txt", "input02.txt", "input03.txt"])
import math


class Rational:
    def __init__(self, n, d=1):
        g = math.gcd(n, d)
        self.n = n // g
        self.d = d // g

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"


class RationalList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            self.data.append(item)
        return self

    def __iter__(self):
        sorted_data = sorted(self.data, key=lambda r: (r.d, r.n), reverse=True)
        return iter(sorted_data)


def main():
    num = input("Виберіть номер файлу (01, 02 або 03): ")
    filename = "input" + num + ".txt"

    r_list = RationalList()

    try:
        f = open(filename, "r")
        for line in f:
            for t in line.split():
                try:
                    if "/" in t:
                        p = t.split("/")
                        r_list += Rational(int(p[0]), int(p[1]))
                    else:
                        r_list += int(t)
                except ValueError:
                    continue
        f.close()

        if len(r_list) == 0:
            print("Чисел не знайдено")
            return

        print("Числа у відсортованому порядку:")
        for item in r_list:
            print(item)

    except FileNotFoundError:
        print("Файл не знайдено!")


main()
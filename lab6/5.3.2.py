import math


class Rational:
    def __init__(self, n, d=1):
        g = math.gcd(n, d)
        self.n = n // g
        self.d = d // g

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"


class RationalList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        new_obj = RationalList()
        new_obj.data = self.data[:]
        if isinstance(other, RationalList):
            new_obj.data.extend(other.data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            new_obj.data.append(item)
        return new_obj

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            self.data.append(item)
        return self


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

        suma = r_list[0]
        for i in range(1, len(r_list)):
            suma = suma + r_list[i]

        print("Результат:", suma)

    except FileNotFoundError:
        print("Файл не знайдено!")


main()
import math


class RationalError(ZeroDivisionError):
    pass


class RationalValueError(ValueError):
    pass


class Rational:
    def __init__(self, n, d=None):
        try:
            if d is None:
                if isinstance(n, str):
                    if '/' in n:
                        parts = n.split('/')
                        n, d = int(parts[0]), int(parts[1])
                    else:
                        n, d = int(n), 1
                elif isinstance(n, Rational):
                    n, d = n.n, n.d
                elif isinstance(n, int):
                    n, d = n, 1
                else:
                    raise ValueError
            else:
                n, d = int(n), int(d)
        except (ValueError, TypeError, IndexError):
            raise RationalValueError("Некоректні дані для Rational")

        if d == 0:
            raise RationalError("Знаменник не може бути нулем")

        common = math.gcd(n, d)
        self.n, self.d = n // common, d // common
        if self.d < 0:
            self.n, self.d = -self.n, -self.d

    def __add__(self, other):
        if not isinstance(other, (Rational, int)):
            raise RationalValueError("Некоректний тип для додавання")
        other = Rational(other) if isinstance(other, int) else other
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __str__(self):
        return f"{self.n}/{self.d}"


class RationalList:
    def __init__(self, items=None):
        self._data = []
        if items:
            for item in items:
                self.append(item)

    def append(self, item):
        if isinstance(item, (int, str, Rational)):
            self._data.append(Rational(item))
        else:
            raise RationalValueError("До списку можна додавати лише Rational, int або дріб-рядок")

    def __getitem__(self, idx):
        return self._data[idx]

    def __setitem__(self, idx, value):
        if not isinstance(value, (Rational, int, str)):
            raise RationalValueError("Некоректні дані для зміни елемента")
        self._data[idx] = Rational(value)

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            for item in other._data: new_list.append(item)
        elif isinstance(other, (Rational, int, str)):
            new_list.append(other)
        else:
            raise RationalValueError("Некоректні дані для конкатенації")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._data: self.append(item)
        elif isinstance(other, (Rational, int, str)):
            self.append(other)
        else:
            raise RationalValueError("Некоректні дані для додавання")
        return self


def solve(file_name):
    rl = RationalList()
    try:
        with open(file_name, 'r') as f:
            for line in f:
                for token in line.split():
                    rl.append(token)

        if len(rl) == 0:
            return "Список порожній"

        total_sum = rl[0]
        for i in range(1, len(rl)):
            total_sum = total_sum + rl[i]
        return total_sum
    except FileNotFoundError:
        return "Файл не знайдено"
    except (RationalError, RationalValueError) as e:
        return f"Помилка: {e}"


for name in ['input01.txt', 'input02.txt', 'input03.txt']:
    print(f"Результат для {name}: {solve(name)}")
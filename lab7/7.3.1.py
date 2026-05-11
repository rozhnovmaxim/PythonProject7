import math


class Rational:
    def __init__(self, n=0, d=1):
        if isinstance(n, str):
            n, d = map(int, n.split('/'))

        common = math.gcd(n, d)
        self._n = n // common
        self._d = d // common

        if self._d < 0:
            self._n *= -1
            self._d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self._n * other._d, self._d * other._n)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n": return self._n
        if key == "d": return self._d

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            self._d = value
        common = math.gcd(self._n, self._d)
        self._n //= common
        self._d //= common

    def __str__(self):
        return f"{self._n}/{self._d}"


def solve_expression(line):
    tokens = line.split()
    items = []
    for t in tokens:
        if t in "+-*/":
            items.append(t)
        else:
            if '/' in t:
                items.append(Rational(t))
            else:
                items.append(Rational(int(t)))

    i = 1
    while i < len(items):
        if items[i] in "*/":
            op = items.pop(i)
            left = items.pop(i - 1)
            right = items.pop(i - 1)
            res = left * right if op == "*" else left / right
            items.insert(i - 1, res)
        else:
            i += 2

    res = items[0]
    for i in range(1, len(items), 2):
        op = items[i]
        next_val = items[i + 1]
        if op == "+":
            res = res + next_val
        else:
            res = res - next_val
    return res


try:
    with open('input01.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                result = solve_expression(line)
                print(f"Result: {result} ({result():.4f})")
except FileNotFoundError:
    pass
import math


class Rational:
    def __init__(self, n=0, d=1):
        if isinstance(n, Rational):
            self.n, self.d = n.n, n.d
        elif isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                self.n, self.d = int(parts[0]), int(parts[1])
            else:
                self.n, self.d = int(n), 1
        else:
            self.n, self.d = n, d
        self.simplify()

    def simplify(self):
        if self.d == 0:
            raise ZeroDivisionError()
        common = math.gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n, self.d = -self.n, -self.d

    def __add__(self, other):
        other = other if isinstance(other, Rational) else Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        other = other if isinstance(other, Rational) else Rational(other)
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)

    def __mul__(self, other):
        other = other if isinstance(other, Rational) else Rational(other)
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        other = other if isinstance(other, Rational) else Rational(other)
        return Rational(self.n * other.d, self.d * other.n)

    def __call__(self):
        return self.n / self.d

    def __repr__(self):
        return f"{self.n}/{self.d}"


def calculate(expr):
    tokens = expr.split()
    values = []
    ops = []

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            values.append(Rational(token))
        else:
            ops.append(token)

    i = 0
    while i < len(ops):
        if ops[i] in ('*', '/'):
            op = ops.pop(i)
            left = values.pop(i)
            right = values.pop(i)
            result = left * right if op == '*' else left / right
            values.insert(i, result)
        else:
            i += 1

    res = values[0]
    for i, op in enumerate(ops):
        if op == '+':
            res = res + values[i + 1]
        elif op == '-':
            res = res - values[i + 1]

    return res


try:
    with open('input01.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                result = calculate(line)
                print(f"{line} = {result} ({result()})")
except:
    pass
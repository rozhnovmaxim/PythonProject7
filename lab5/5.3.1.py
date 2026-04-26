import

class Rational:
    def __init__(self, n=0, d=1):
        if isinstance(n, Rational):
            self.n = n.n
            self.d = n.d
        elif isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                self.n = int(parts[0])
                self.d = int(parts[1])
            else:
                self.n = int(n)
                self.d = 1
        else:
            self.n = n
            self.d = d
        self.simplify()

    def simplify(self):
        common = math.gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(self.n * other.d, self.d * other.n)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n': return self.n
        if key == 'd': return self.d

    def __setitem__(self, key, value):
        if key == 'n': self.n = value
        elif key == 'd': self.d = value
        self.simplify()

    def __repr__(self):
        return f"{self.n}/{self.d}"

def calculate(expr):
    tokens = expr.split()
    res = Rational(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        next_val = Rational(tokens[i+1])
        if op == '+': res = res + next_val
        elif op == '-': res = res - next_val
        elif op == '*': res = res * next_val
        elif op == '/': res = res / next_val
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
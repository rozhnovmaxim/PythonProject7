import math


class RationalError(ZeroDivisionError):
    pass


class RationalValueError(ValueError):
    pass


class Rational:
    def __init__(self, n=0, d=1):
        if isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        elif isinstance(n, str):
            parts = n.split('/')
            self._n = int(parts[0])
            self._d = int(parts[1]) if len(parts) > 1 else 1
        else:
            self._n = n
            self._d = d

        if self._d == 0:
            raise RationalError("Denominator cannot be zero")

        self._simplify()

    def _simplify(self):
        common = math.gcd(self._n, self._d)
        self._n //= common
        self._d //= common
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def _check_operand(self, other):
        if isinstance(other, int):
            return Rational(other)
        if isinstance(other, Rational):
            return other
        raise RationalValueError(f"Unsupported operand type: {type(other).__name__}")

    def __add__(self, other):
        other = self._check_operand(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __sub__(self, other):
        other = self._check_operand(other)
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __mul__(self, other):
        other = self._check_operand(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        other = self._check_operand(other)
        if other._n == 0:
            raise RationalError("Division by zero in rational arithmetic")
        return Rational(self._n * other._d, self._d * other._n)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n": return self._n
        if key == "d": return self._d
        raise KeyError

    def __setitem__(self, key, value):
        if key == "n":
            self._n = value
        elif key == "d":
            if value == 0:
                raise RationalError("Denominator cannot be zero")
            self._d = value
        else:
            raise KeyError
        self._simplify()

    def __str__(self):
        return f"{self._n}/{self._d}"


def evaluate_expression(expr):
    tokens = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').split()
    processed_tokens = []
    for t in tokens:
        if t in "+-*":
            processed_tokens.append(t)
        else:
            processed_tokens.append(Rational(t))

    def apply_ops(ops_to_do):
        i = 1
        while i < len(processed_tokens):
            if processed_tokens[i] in ops_to_do:
                left = processed_tokens[i - 1]
                op = processed_tokens[i]
                right = processed_tokens[i + 1]
                if op == '*':
                    result = left * right
                elif op == '+':
                    result = left + right
                elif op == '-':
                    result = left - right
                processed_tokens[i - 1:i + 2] = [result]
            else:
                i += 2

    apply_ops(['*'])
    apply_ops(['+', '-'])
    return processed_tokens[0]


def main():
    filename = 'input01.txt'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"File {filename} is empty.")
                return
            for line in lines:
                line = line.strip()
                if line:
                    result = evaluate_expression(line)
                    print(f"Expression: {line}")
                    print(f"Result: {result} ({result()})\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found in the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
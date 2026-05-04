import math


class MathProblemsSolver:
    def solve_a(self, x, k):
        return (x ** (2 * k)) / math.factorial(2 * k)

    def solve_b(self, n):
        product = 1.0
        for i in range(1, n + 1):
            product *= (1 + 1 / (i ** 2))
        return product

    def solve_c(self, n, a, b):
        if n == 0: return 1
        if n == 1: return a + b
        det_prev2 = 1
        det_prev1 = a + b
        current_det = det_prev1
        for _ in range(2, n + 1):
            current_det = (a + b) * det_prev1 - (a * b) * det_prev2
            det_prev2 = det_prev1
            det_prev1 = current_det
        return current_det

    def solve_d(self, n):
        if n < 1: return 0
        a = [0] * (max(4, n + 1))
        a[1] = a[2] = a[3] = 1
        for k in range(4, n + 1):
            a[k] = a[k - 1] + a[k - 3]
        s_n = sum(a[k] / (2 ** k) for k in range(1, n + 1))
        return s_n

    def solve_e(self, x, eps):
        if not (-1 < x < 1):
            return None, None
        sum_series = 0
        k = 0
        while True:
            term = (x ** (2 * k + 1)) / (2 * k + 1)
            if abs(2 * term) < eps:
                break
            sum_series += term
            k += 1
        taylor_result = 2 * sum_series
        math_result = math.log((1 + x) / (1 - x))
        return taylor_result, math_result


if __name__ == "__main__":
    solver = MathProblemsSolver()

    val_x_a, val_k_a = 2.0, 3
    print(f"a) x_k = {solver.solve_a(val_x_a, val_k_a)}")

    val_n_b = 5
    print(f"b) P_n = {solver.solve_b(val_n_b)}")

    val_n_c, val_a_c, val_b_c = 3, 2, 3
    print(f"c) Det = {solver.solve_c(val_n_c, val_a_c, val_b_c)}")

    val_n_d = 10
    print(f"d) S_n = {solver.solve_d(val_n_d)}")

    val_x_e, val_eps_e = 0.5, 1e-7
    t_res, m_res = solver.solve_e(val_x_e, val_eps_e)
    print(f"e) Taylor: {t_res}, Math Lib: {m_res}, Diff: {abs(t_res - m_res)}")
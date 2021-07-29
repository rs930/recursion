from util import calc_time
import matplotlib.pyplot as plt
"""
Run fibonacci 3 ways
1) Recursion 2) Iteration 3) Recursion with Dynamic Programming
"""


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)


def fib_rec_dy(n, memoiz={0: 0, 1: 1}):
    m = memoiz.get(n)
    if m is None:
        fib = fib_rec_dy(n-2, memoiz) + fib_rec_dy(n-1, memoiz)
        memoiz[n] = fib
        return fib
    else:
        return m


def fib_iter(n):
    fib0 = 0
    fib1 = 1
    i = 1
    if n <= 0:
        return 0
    while i < n:
        fib = fib1 + fib0
        fib0 = fib1
        fib1 = fib
        i += 1
    return fib1


if __name__ == '__main__':
    test_values = range(1, 20, 2)
    t_rec = []
    t_iter = []
    t_rec_dy = []

    for v in test_values:
        t_rec.append(calc_time(fib_rec, v))
        t_iter.append(calc_time(fib_iter, v))
        t_rec_dy.append(calc_time(fib_rec_dy, v))

    plt.figure(figsize=(8, 5));
    plt.plot(test_values, t_rec, 'go-', label='recursion')
    plt.plot(test_values, t_iter, 'bo-', label='iteration')
    plt.plot(test_values, t_rec_dy, 'ro-', label='recursion_dyn')
    plt.title('Fibonacci Calculation')
    plt.ylabel('time/(s)')
    plt.xlabel('n')
    plt.grid()
    plt.legend()
    plt.show()

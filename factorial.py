import matplotlib.pyplot as plt
from util import calc_time
"""
Run factorial two ways Recursion and Iterations
Iteration is faster due to less memory operations
"""


def fact_rec(n):
    """
    :param n: positive number
    :return:
    """
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n-1)


def fact_iter(n):
    """
    :param n:
    :return:
    """
    i = 1
    for k in range(1, n+1):
        i = i*k
    return i


if __name__ == '__main__':
    test_values = range(0, 1000, 50)
    t_rec = []
    t_iter = []
    for v in test_values:
        t_rec.append(calc_time(fact_rec, v))
        t_iter.append(calc_time(fact_iter, v))

    plt.figure(figsize=(8, 5));
    plt.plot(test_values, t_rec, 'go-', label='recursion')
    plt.plot(test_values, t_iter, 'bo-', label='iteration')
    plt.title('Factorial Calculation')
    plt.ylabel('time/(s)')
    plt.xlabel('n')
    plt.grid()
    plt.legend()
    plt.show()

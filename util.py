import time


def calc_time(func, n, trials=100):
    """
    calculates avg time taken for func to operate on n
    :param func:
    :param n: value on which func will operate
    :param trials: number of iterations to avg time
    :return: time in seconds
    """
    i = 0
    t0 = time.perf_counter()
    while i < trials:
        func(n);
        i += 1
    t1 = time.perf_counter()
    return (t1 - t0)/trials


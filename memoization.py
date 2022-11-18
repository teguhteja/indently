from functools import wraps
from time import perf_counter
import sys

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper

@memoize
def fib(n) -> int:
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    sys.setrecursionlimit(10_000)
    
    start = perf_counter()
    f = fib(2000)
    end = perf_counter()

    print(f)
    print(f'Time : {end-start} s')
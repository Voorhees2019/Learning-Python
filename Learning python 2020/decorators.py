from timeit import default_timer
import math


def measure_time(func):
    def wrap(*args, **kwargs):
        print(f'Calling func {func.__name__}')
        start = default_timer()
        func(*args, **kwargs)
        end = default_timer()
        print(f'Func {func.__name__} took {end - start} for execution')
    return wrap


@measure_time
def factorial(n):
    print(math.factorial(5))


factorial(5)
help(factorial)
print('--------------------------------------------------------------')
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func {func.__name__}')
        start = default_timer()
        func(*args, **kwargs)
        end = default_timer()
        print(f'Func {func.__name__} took {end - start} for execution')
    return wrap


@measure_time
def factorial(n):
    print(math.factorial(5))


factorial(5)
help(factorial)








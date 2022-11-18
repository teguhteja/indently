from functools import wraps
from time import perf_counter, sleep

def get_time(func):
    """Times any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time-start_time,2)

        print('Time', total_time, 'second')

    return wrapper

@get_time
def do_something(param: str):
    """Do something important"""

    sleep(1)
    print(param)


if __name__ ==  '__main__':
    do_something('Hello')

    print(do_something.__name__)
    print(do_something.__doc__)
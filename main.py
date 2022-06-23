import datetime
import os
import functools


def logger(log_path):
    log_path = os.path.abspath(log_path)
    if log_path[-1] != '/':
        log_path += '/'

    def logger_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(log_path + 'log.{}'.format(func.__name__) +
                      '.{}'.format(datetime.datetime.now())[:20].replace(':', '-') + '.log', 'w') as l:
                l.write(f'function_name = "{func.__name__}"\n'
                        f'function_args = "{args}" and "{kwargs}"\n'
                        f'function_start_date = "{datetime.date.today()}"\n'
                        f'function_start_time = "{datetime.datetime.now().time()}"\n')
                result = func(*args, **kwargs)
                l.write(f'function_result = "{result}"')

        return wrapper

    return logger_decorator


@logger(log_path=input("Input log saving path :"))
def test_func(a, b, c):
    return a * b + c


if __name__ == '__main__':
    test_func(1, 2, 3)

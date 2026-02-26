import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def timer_decorator(func):
    """Декоратор, що вимірює час виконання функції."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        logging.info(f"Функція '{func.__name__}' виконана за {execution_time:.4f} сек.")

        return result, execution_time

    return wrapper


@timer_decorator
def heavy_computation(n):
    """Функція для тестування: імітація складних обчислень."""
    total = 0
    for i in range(n):
        total += i
    time.sleep(0.1)
    return total
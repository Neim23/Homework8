import unittest
import time
from main import heavy_computation, timer_decorator


class TestTimerDecorator(unittest.TestCase):

    def test_return_value(self):
        """Перевірка, чи функція повертає правильний математичний результат."""
        result, exec_time = heavy_computation(10)
        self.assertEqual(result, 45)  # Сума 0..9 = 45

    def test_execution_time_positive(self):
        """Перевірка, чи зафіксований час більший за нуль."""
        _, exec_time = heavy_computation(100)
        self.assertGreater(exec_time, 0)

    def test_timing_accuracy(self):
        """Перевірка, чи декоратор фіксує затримку (sleep)."""

        @timer_decorator
        def slow_func():
            time.sleep(0.2)
            return True

        _, exec_time = slow_func()
        # Время минимум 0.2 не забудь
        self.assertGreaterEqual(exec_time, 0.2)


if __name__ == '__main__':
    unittest.main()
from unittest import TestCase

from basic_lab1.fibonacci_number import Solution


class TestSolution(TestCase):
    def test_fib_pythonic(self):
        s = Solution()
        # 对数器
        for i in range(100):
            self.assertEqual(s.fib_dp(i), s.fib_pythonic(i))

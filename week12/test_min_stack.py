from unittest import TestCase

from week12.min_stack import MinStack


class TestMinStack(TestCase):
    def test_push(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        print(obj.getMin())
        obj.pop()
        print(obj.top())
        print(obj.getMin())
        param_3 = obj.top()
        param_4 = obj.getMin()

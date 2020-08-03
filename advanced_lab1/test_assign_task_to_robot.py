from unittest import TestCase

from advanced_lab1.assign_task_to_robot import assign_task


class Test(TestCase):
    def test_assign_task(self):
        self.assertEqual((1, 20006), assign_task([(100, 3)], [(100, 2), (100, 1)]))

from typing import List
from unittest import TestCase

from basic_lab2.last_survivor import last


class Test(TestCase):
    def test_last(self):
        self.assertEqual(255,last(500))

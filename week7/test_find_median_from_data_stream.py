from typing import List
from unittest import TestCase

from week7.find_median_from_data_stream import MedianFinder


class TestMedianFinder(TestCase):
    def test_find_median(self):
        m = MedianFinder()
        m.addNum(1)
        m.addNum(2)
        self.assertEqual(1.5, m.findMedian())
        m.addNum(3)
        self.assertEqual(2, m.findMedian())

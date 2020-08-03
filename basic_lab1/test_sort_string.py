from unittest import TestCase

from basic_lab1.sort_string import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual('epTy', solution('Type'))
        self.assertEqual('aABb', solution('BabA'))
        self.assertEqual('Be?y', solution('By?e'))
        self.assertEqual('A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).', solution('A Famous Saying: Much Ado About Nothing (2012/8).'))

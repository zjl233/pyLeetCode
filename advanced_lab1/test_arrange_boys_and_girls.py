from unittest import TestCase

from advanced_lab1.arrange_boys_and_girls import arrange


class Test(TestCase):
    def test_arrange(self):
        self.assertEqual(2, arrange('GGBBG'))

from unittest import TestCase

from advanced_lab1.painter_xiaoq import painting_steps


class Test(TestCase):
    def test_painting_steps(self):
        board = [
            ['Y', 'X', 'X', 'B', ],
            ['X', 'Y', 'G', 'X', ],
            ['X', 'B', 'Y', 'Y', ],
            ['B', 'X', 'X', 'Y', ],
        ]
        self.assertEqual(3, painting_steps(board))
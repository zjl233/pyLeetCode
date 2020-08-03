from unittest import TestCase

from week7.meeting_rooms_ii import Solution


class TestSolution(TestCase):
    def test_min_meeting_rooms(self):
        s = Solution()
        self.assertEqual(2, s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(1, s.minMeetingRooms([[7, 10], [2, 4]]))

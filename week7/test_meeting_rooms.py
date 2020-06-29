from unittest import TestCase

from week7.meeting_rooms import Solution


class TestSolution(TestCase):
    def test_can_attend_meetings(self):
        s = Solution()
        self.assertFalse(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(s.canAttendMeetings([[7, 10], [2, 4]]))

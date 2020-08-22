from unittest import TestCase

from week8.restore_ip_addresses import Solution


class TestSolution(TestCase):
    def test_restore_ip_addresses(self):
        s = Solution()
        expect1 = ["255.255.11.135", "255.255.111.35"]
        res1 = s.restoreIpAddresses("25525511135")
        self.assertEqual(expect1, res1)

        expect2 = ["0.0.0.0"]
        res2 = s.restoreIpAddresses("0000")
        self.assertEqual(expect2, res2)

        expect3 = ["1.1.1.1"]
        res3 = s.restoreIpAddresses("1111")
        self.assertEqual(expect3, res3)

        expect4 = ["0.10.0.10", "0.100.1.0"]
        res4 = s.restoreIpAddresses("010010")
        self.assertEqual(expect4, res4)

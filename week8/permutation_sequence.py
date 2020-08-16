class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        选择路径
        https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
        :param n:
        :param k:
        :return:
        """
        nums = [str(i) for i in range(1, n + 1)]

        fact = [1 for i in range(n + 1)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        k -= 1
        res = ""
        for i in range(n - 1, -1, -1):
            choice = k // fact[i]
            k -= fact[i] * choice
            res += nums.pop(choice)

        return res

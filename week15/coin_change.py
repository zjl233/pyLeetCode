from typing import List, Union


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        res = self.process(coins, amount, 0)
        return res if res != float('inf') else -1

    def process(self, coins: List[int], amount: int, cnt: int) -> Union[int, float]:
        if amount < 0:
            return float('inf')

        if amount == 0:
            return cnt

        min_ = float('inf')
        for c in coins:
            res = self.process(coins, amount - c, cnt + 1)
            min_ = min(min_, res)

        return min_

    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

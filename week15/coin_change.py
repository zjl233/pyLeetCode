from typing import List, Union


class Solution:
    # 第一中思路，每次都取一张，尝试取遍 coins 里的每一种 coin

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        res = self.process(coins, amount, 0)
        return res if res != float('inf') else -1

    # 无法使用 memo，因为
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

    # 还有另一种思路，每次都取一种，取无数张
    def coin_change(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 or amount < 0:
            return 0

        self.dfs(coins, 0, amount)

    def dfs(self, coins: List[int], idx: int, amount: int):
        if idx == len(coins):
            return 1 if amount == 0 else 0

        ways = 0
        zhang = 0
        while zhang * coins[idx] <= amount:
            ways += self.dfs(coins, idx + 1, amount - zhang * coins[idx])
            zhang += 1

        return ways

    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        # 这里跳了一步，空间压缩后的 dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

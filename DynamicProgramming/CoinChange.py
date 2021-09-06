# Approach-1

import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        for i in range(0, amount+1):
            dp[0][i] = sys.maxsize

        for i in range(1, amount+1):
            if i % coins[0] == 0:
                dp[1][i] = i / coins[0]
            else:
                dp[1][i] = sys.maxsize

        for i in range(2, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1 + dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        if dp[-1][-1] >= sys.maxsize:
            return -1
        else:
            return int(dp[-1][-1])


# Approach-2

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        # coins.sort()
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1+dp[i-coins[j]])
                else:
                    break

        return -1 if dp[amount] > amount else dp[amount]

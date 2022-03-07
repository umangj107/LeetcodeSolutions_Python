import math


class Solution:
    def countOrders(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 6
        dp = [0 for _ in range(n+1)]
        mod = math.pow(10, 9) + 7
        dp[0] = 0
        dp[1] = 1
        dp[2] = 6
        for i in range(3, n+1):
            oddno = 2 * i - 1
            perm = oddno * (oddno + 1) // 2
            dp[i] = (dp[i-1] * perm) % mod
        return int(dp[n])

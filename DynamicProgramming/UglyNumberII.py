class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1, n):
            dp[i] = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            if dp[i] == dp[i2]*2:
                i2 += 1
            if dp[i] == dp[i3]*3:
                i3 += 1
            if dp[i] == dp[i5]*5:
                i5 += 1
        return dp[-1]

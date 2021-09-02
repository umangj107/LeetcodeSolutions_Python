# Approach-1
# Recursive-Approach
# Gives TLE

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


# Approach-2
# DP-Approach

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            dp = [0 for _ in range(n+1)]
            dp[1], dp[2], dp[3] = 1, 2, 3
            for i in range(4, n+1):
                dp[i] = dp[i-1] + dp[i-2]

            return dp[n]

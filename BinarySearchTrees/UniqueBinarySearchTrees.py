# Approach-1

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            for j in range(1, i+1):
                dp[i] = dp[i] + (dp[i-j] * dp[j-1])

        return dp[-1]


# Approach-2

class Solution:
    def numTrees(self, n: int) -> int:
        x = math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))
        return int(x)

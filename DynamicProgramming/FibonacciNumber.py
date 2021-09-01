# Approach-1

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        for i in range(2, n+1):
            temp = a + b
            a = b
            b = temp

        return b


# Approach-2

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp = [0 for _ in range(n+1)]
            dp[0] = 0
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]

            return dp[-1]

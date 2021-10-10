class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        lastOcc = {}
        for i in range(1, n+1):
            dp[i] = 2 * dp[i-1]
            if s[i-1] in lastOcc:
                dp[i] -= dp[lastOcc[s[i-1]]-1]
            lastOcc[s[i-1]] = i

        return (dp[-1] - 1) % 1000000007

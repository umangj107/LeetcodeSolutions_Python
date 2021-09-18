# Approach-1
# DP Approach

class Solution:
    def LCS(self, s, t, m, n):
        if m == 0 or n == 0:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m > n:
            return False
        elif self.LCS(s, t, m, n) == m:
            return True
        return False


# Approach-2

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        sIndex = 0
        tIndex = 0

        while sIndex < m and tIndex < n:
            if t[tIndex] == s[sIndex]:
                sIndex += 1
            tIndex += 1

        if sIndex != m:
            return False
        return True

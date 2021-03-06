class Solution:
    def LCS(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0
        else:
            dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        lcs = self.LCS(word1, word2, m, n)

        if lcs == n:
            return abs(m - lcs)
        else:
            return abs(m - lcs) + abs(n - lcs)

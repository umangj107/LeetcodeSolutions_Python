# Approach-1
# Dp Approach

class Solution:
    def LCS(self, s1, s2, m):
        if m == 0:
            return 0
        else:
            dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, m+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[m][m]

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.LCS(s, s[::-1], len(s))


# Approach-2
# Efficient Approach

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return 1

        @lru_cache(None)
        def solve(s):
            if s == s[::-1]:
                return len(s)
            else:
                ml = 0
                for i in set(s):
                    l = s.find(i)
                    r = s.rfind(i)
                    ml = max(ml, 1 if l == r else 2+solve(s[l+1:r]))

                return ml

        return solve(s)

class Solution:
    def LCS(self, s1, s2, m, n):
        if m == 0:
            return 0
        else:
            dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = self.LCS(str1, str2, m, n)
        result = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result += str1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    result += str1[i-1]
                    i -= 1
                elif dp[i][j-1] >= dp[i-1][j]:
                    result += str2[j-1]
                    j -= 1
        while i > 0:
            result += str1[i-1]
            i -= 1

        while j > 0:
            result += str2[j-1]
            j -= 1

        return result[::-1]

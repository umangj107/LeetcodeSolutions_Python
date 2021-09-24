# Approach-1
# Brute Force

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        out = []
        for i in range(0, n):
            for j in range(i+1, n+1):
                out.append(s[i:j])
        c = 0
        for i in out:
            if i == i[::-1]:
                c += 1
        return c


# Approach-2
# DP-Approach

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        countTrue = 0
        for i in range(len(s)):
            dp[i][i] = True
            countTrue += 1

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                countTrue += 1

        for gap in range(2, len(s)):
            for i in range(len(s)-gap):
                j = i + gap
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    countTrue += 1

        return countTrue

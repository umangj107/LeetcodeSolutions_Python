# Approach-1
# DP

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m == 0:
            return 0

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = int(matrix[0][0])

        height = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    height = max(height, dp[i][j])

        return height**2


# Approach-2
# Optimized DP

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        height = 0
        curr = [0 for _ in range(n+1)]
        prev = [0 for _ in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    curr[j] = 1 + min(curr[j-1], prev[j-1], prev[j])
                    height = max(height, curr[j])

            prev = curr[:]
            curr = [0 for _ in range(n+1)]
        return height ** 2

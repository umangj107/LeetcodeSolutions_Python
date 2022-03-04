# Approach-1

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * k for k in range(1, 102)]
        dp[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i+1):
                q = (dp[i][j] - 1.0) / 2.0
                if q > 0:
                    dp[i+1][j] += q
                    dp[i+1][j+1] += q

        return min(1.0, dp[query_row][query_glass])


# Approach-2

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        for row in range(1, query_row + 1):
            next = [0.0] * (row + 1)
            for i in range(len(curr)):
                remaining = curr[i] - 1.0
                if remaining > 0.0:
                    q = remaining / 2
                    next[i] += q
                    next[i+1] += q
            curr = next

        return min(1.0, curr[query_glass])

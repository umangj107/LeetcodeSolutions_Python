# Approach-1
# Recursive Approach

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 99999
            elif i == len(matrix) - 1:
                return matrix[i][j]
            else:
                return matrix[i][j]+min(helper(i+1, j-1), min(helper(i+1, j), helper(i+1, j+1)))

        min_sum = 99999
        for col in range(len(matrix[0])):
            min_sum = min(helper(0, col), min_sum)
        return min_sum


# Approach-2
# DP Approach

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dp[-1] = matrix[-1]

        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])):
                x = dp[i+1][j-1] if j-1 >= 0 else 99999
                y = dp[i+1][j]
                z = dp[i+1][j+1] if j+1 < len(matrix[0]) else 99999
                dp[i][j] = matrix[i][j] + min(x, min(y, z))
        # print(dp)
        return min(dp[0])

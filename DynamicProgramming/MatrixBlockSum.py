class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return mat
        else:
            n = len(mat)
            m = len(mat[0])
            dp = [[0 for _ in range(m)] for _ in range(n)]
            dp[0][0] = mat[0][0]
            for i in range(1, n):
                dp[i][0] = dp[i-1][0] + mat[i][0]
            for j in range(1, m):
                dp[0][j] = dp[0][j-1] + mat[0][j]

            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - \
                        dp[i-1][j-1] + mat[i][j]

            result = [[0 for _ in range(m)] for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    minRow, minCol = i - k - 1, j - k - 1
                    maxRow, maxCol = min(n - 1, i + k), min(m - 1, j + k)

                    topLeft = dp[minRow][minCol] if minRow >= 0 and minCol >= 0 else 0
                    topRight = dp[minRow][maxCol] if minRow >= 0 else 0
                    bottomLeft = dp[maxRow][minCol] if minCol >= 0 else 0
                    bottomRight = dp[maxRow][maxCol]

                    result[i][j] = bottomRight + \
                        topLeft - bottomLeft - topRight

            return result

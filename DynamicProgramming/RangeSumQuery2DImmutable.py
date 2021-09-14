class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dp = [[0 for _ in range(self.cols+1)] for _ in range(self.rows+1)]

        # Creating cumulative sum matrix as dp
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.dp[i+1][j+1] = self.dp[i+1][j] + \
                    self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

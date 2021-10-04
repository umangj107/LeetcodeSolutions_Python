class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] != 0:
                money = grid[row][col]
                grid[row][col] = 0
                ans = max(dfs(row+1, col), dfs(row-1, col),
                          dfs(row, col+1), dfs(row, col-1)) + money
                grid[row][col] = money
                return ans
            else:
                return 0

        answer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    answer = max(answer, dfs(i, j))

        return answer

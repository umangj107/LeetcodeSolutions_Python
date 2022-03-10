class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.count = 0
        res = 0

        def dfs(i, j):
            if grid[i][j] == 0 or grid[i][j] == -1:
                return True
            if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                return False
            grid[i][j] = -1
            self.count += 1
            l = dfs(i, j-1)
            t = dfs(i-1, j)
            r = dfs(i, j+1)
            b = dfs(i+1, j)
            return l and t and r and b

        count = 0
        for r in range(rows):
            for c in range(cols):
                self.count = 0
                if grid[r][c] == 1 and dfs(r, c):
                    res += self.count

        return res

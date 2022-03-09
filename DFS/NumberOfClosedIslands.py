class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        self.visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            else:
                if grid[i][j] == 1:
                    return True

                elif self.visited[i][j] == True:
                    return False

                grid[i][j] = 1
                self.visited[i][j] = True
                D = dfs(i+1, j)
                R = dfs(i, j+1)
                U = dfs(i-1, j)
                L = dfs(i, j-1)
                return D and R and L and U

        count = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0 and not self.visited[x][y]:
                    if dfs(x, y):
                        count += 1
        return count

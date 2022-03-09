class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def getArea(x, y):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + getArea(x+1, y) + getArea(x-1, y) + getArea(x, y+1) + getArea(x, y-1)
            else:
                return 0

        maxArea = 0
        area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = getArea(i, j)
                    maxArea = max(area, maxArea)
        return maxArea

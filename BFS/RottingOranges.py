class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        minute = 0
        while queue:
            temp = []
            while queue:
                r, c, minute = queue.pop(0)
                for row, col in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    if 0 <= row < n and 0 <= col < m and grid[row][col] == 1:
                        temp.append((row, col, minute+1))
                        grid[row][col] = 2
            queue = temp

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return minute

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        curr_dist = -1
        queue = []

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == rows * cols:
            return -1

        while queue:
            temp = []
            curr_dist += 1
            while queue:
                x, y = queue.pop(0)
                for r, c in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                        temp.append((r, c))
                        grid[r][c] = 1
            queue = temp

        return curr_dist

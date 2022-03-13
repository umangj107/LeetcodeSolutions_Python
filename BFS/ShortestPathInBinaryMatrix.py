class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows * cols == 1:
            return 1 if grid[0][0] == 0 else -1

        if grid[0][0] == 1 or (grid[1][0] == 1 and grid[0][1] == 1 and grid[1][1] == 1) or grid[rows-1][cols-1] == 1:
            return -1

        curr_moves = 1

        queue = [(0, 0)]
        grid[0][0] = 1
        val = grid[0][0]

        while queue:
            temp = []
            while queue:
                x, y = queue.pop(0)
                if x == rows-1 and y == cols-1:
                    return curr_moves
                for r, c in [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                        temp.append((r, c))
                        grid[r][c] = 1
            curr_moves += 1
            queue = temp

        return -1

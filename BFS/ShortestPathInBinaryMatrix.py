class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1

        queue = [(0, 0)]
        moves = 1

        while queue:
            tempQueue = []
            while queue:
                x, y = queue.pop(0)
                if x == n-1 and y == n-1:
                    return moves
                for i, j in [(x, y+1), (x, y-1), (x+1, y), (x-1, y),
                             (x+1, y-1), (x-1, y+1), (x+1, y+1), (x-1, y-1)]:
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        tempQueue.append((i, j))
                        grid[i][j] = 1

            moves += 1
            queue = tempQueue

        return -1

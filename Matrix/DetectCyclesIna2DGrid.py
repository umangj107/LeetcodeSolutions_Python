class Solution:
    def adjNodes(self, grid, r, c):
        nodes = []
        for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                nodes.append((i, j))
        return nodes

    def isCycle(self, grid, r, c, prev, letter):
        grid[r][c] = ord(letter)

        for i, j in self.adjNodes(grid, r, c):
            if prev != (i, j):
                val = grid[i][j]
                if val == letter:
                    if self.isCycle(grid, i, j, (r, c), letter):
                        return True
                elif val == ord(letter):
                    return True

        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if type(grid[i][j]) is str:
                    if self.isCycle(grid, i, j, ('tmp', 'tmp'), grid[i][j]):
                        return True

        return False

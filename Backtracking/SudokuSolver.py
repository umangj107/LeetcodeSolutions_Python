class Solution:
    # Helper Function to find first empty location in the board
    def findEmptyLoc(self, board, l):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    l[0] = i
                    l[1] = j
                    return True
        return False

    # Helper Function to check if the given value is already used in the same row or same col
    def usedInRowCol(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val or board[i][col] == val:
                return True
        return False

    # Helper Function to check if the given value is already used in the same box
    def usedInBox(self, board, row, col, val):
        for i in range(3):
            for j in range(3):
                if board[row + i][col + j] == val:
                    return True
        return False

    # Helper Function to check if the given location is safe to place the given value
    def isSafe(self, board, r, c, val):
        if not self.usedInRowCol(board, r, c, val) and not self.usedInBox(board, r - r % 3, c - c % 3, val):
            return True
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        l = [0, 0]

        if not self.findEmptyLoc(board, l):
            return True

        r = l[0]
        c = l[1]

        for i in range(1, 10):
            if self.isSafe(board, r, c, str(i)):
                board[r][c] = str(i)
                if self.solveSudoku(board):
                    return True
                board[r][c] = "."

        return False

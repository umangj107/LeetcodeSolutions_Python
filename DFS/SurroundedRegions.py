class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            board[i][j] = '*'

            for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == 'O':
                    dfs(board, x, y)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][-1] == 'O':
                dfs(board, i, len(board[0])-1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(board, 0, j)
            if board[-1][j] == 'O':
                dfs(board, len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        
        def addToResult(n):
            subRes = []
            for row in self.board:
                subStr = ""
                for ele in row:
                    subStr += ele
                subRes.append(subStr)
            self.result.append(subRes)
        
        def isSafe(currRow, currCol, n):
            for i in range(currRow):
                if self.board[i][currCol] == 'Q':
                    return False
            for i,j in zip(range(currRow,-1,-1),range(currCol,-1,-1)):
                if self.board[i][j] == 'Q':
                    return False
            for i, j in zip(range(currRow,-1,-1),range(currCol,n)):
                if self.board[i][j] == 'Q':
                    return False
                
            return True
        
        
        def backtrack(currRow, n):
            if currRow == n:
                addToResult(n)
                return
            else:
                for col in range(n):
                    if isSafe(currRow, col, n):
                        self.board[currRow][col] = 'Q'
                        backtrack(currRow+1, n)
                        self.board[currRow][col] = '.'
                        
                        
        backtrack(0, n)
        return self.result
                        
                    
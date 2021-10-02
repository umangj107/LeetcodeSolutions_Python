# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         self.result = []
#         self.board = [['.' for _ in range(n)] for _ in range(n)]

#         def addToResult(n):
#             subRes = []
#             for row in self.board:
#                 subStr = ""
#                 for ele in row:
#                     subStr += ele
#                 subRes.append(subStr)
#             self.result.append(subRes)

#         def isSafe(currRow, currCol, n):
#             for i in range(currRow):
#                 if self.board[i][currCol] == 'Q':
#                     return False
#             for i,j in zip(range(currRow,-1,-1),range(currCol,-1,-1)):
#                 if self.board[i][j] == 'Q':
#                     return False
#             for i, j in zip(range(currRow,-1,-1),range(currCol,n)):
#                 if self.board[i][j] == 'Q':
#                     return False

#             return True


#         def backtrack(currRow, n):
#             if currRow == n:
#                 addToResult(n)
#                 return
#             else:
#                 for col in range(n):
#                     if isSafe(currRow, col, n):
#                         self.board[currRow][col] = 'Q'
#                         backtrack(currRow+1, n)
#                         self.board[currRow][col] = '.'


#         backtrack(0, n)
#         return self.result


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.cols = set()
        self.posDiagonal = set()
        self.negDiagonal = set()
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.result = []

        def addToResult():
            tempRes = [''.join(row) for row in self.board]
            self.result.append(tempRes)

        def backtrack(r):
            if r == n:
                addToResult()
                return
            else:
                for c in range(n):
                    if c not in self.cols and (r-c) not in self.negDiagonal and (r+c) not in self.posDiagonal:
                        self.cols.add(c)
                        self.posDiagonal.add(r+c)
                        self.negDiagonal.add(r-c)
                        self.board[r][c] = 'Q'

                        backtrack(r+1)

                        self.board[r][c] = '.'
                        self.cols.remove(c)
                        self.posDiagonal.remove(r+c)
                        self.negDiagonal.remove(r-c)

        backtrack(0)
        return self.result

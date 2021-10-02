class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cols = set()
        self.posDiagonal = set()
        self.negDiagonal = set()
        self.res = 0

        def backtrack(r):
            if r == n:
                self.res += 1
                return
            else:
                for c in range(n):
                    if c not in self.cols and (r-c) not in self.negDiagonal and (r+c) not in self.posDiagonal:
                        self.cols.add(c)
                        self.posDiagonal.add(r+c)
                        self.negDiagonal.add(r-c)

                        backtrack(r+1)

                        self.cols.remove(c)
                        self.posDiagonal.remove(r+c)
                        self.negDiagonal.remove(r-c)

        backtrack(0)
        return self.res

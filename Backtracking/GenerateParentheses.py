class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        self.result = []

        def solve(op, ob, cb):
            if ob == 0 and cb == 0:
                self.result.append(op)
                return
            else:
                if ob > 0:
                    op += '('
                    solve(op, ob-1, cb)
                    op = op[:-1]

                if cb > 0 and cb > ob:
                    op += ')'
                    solve(op, ob, cb-1)
                    op = op[:-1]
            return

        solve("", n, n)
        return self.result

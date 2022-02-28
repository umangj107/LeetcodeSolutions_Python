class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                 (2, 1), (-2, 1), (-2, -1), (2, -1)]

        @lru_cache(None)
        def dfs(r, c, k):
            if 0 <= r < n and 0 <= c < n:
                if k == 0:
                    return 1
                ans = 0
                for move in moves:
                    ans += dfs(r + move[0], c + move[1], k-1)
                return ans/8

            return 0

        return dfs(row, column, k)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.memo = {}

        def solve(d, t):
            if d == 0:
                return 0 if t > 0 else 1
            if (d, t) in self.memo:
                return self.memo[(d, t)]

            res = 0
            for i in range(max(0, t-k), t):
                res += solve(d-1, i)

            self.memo[(d, t)] = res % 1000000007
            return self.memo[(d, t)]

        return solve(n, target)

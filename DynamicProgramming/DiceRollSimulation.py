class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 1000000007

        # initiated a dp arry to store the count of all status after first round.
        # dp[n][k] means the number n has occurred k times consecutively before this round
        dp = [[1] + [0] * (min(n, rollMax[i]) - 1) for i in range(6)]
        sums = [1] * 6

        for _ in range(n - 1):
            # every count of status dp[i][j] could be aggregated to dp[k][0] if k != i
            # preprocess a "sums" array to help calculating dp[k][0] for each k later
            for i in range(6):
                sums[i] = sum(dp[i]) % MOD

            total = sum(sums) % MOD

            for cur, row in enumerate(dp):
                # update dp[k][j] by dp[k][j - 1] for j > 0
                for i in range(len(row) - 1, 0, -1):
                    row[i] = row[i - 1]

                # update dp[k][0] by dp[h] where h != k
                row[0] = (total - sums[cur]) % MOD

        return sum(sum(row) % MOD for row in dp) % MOD

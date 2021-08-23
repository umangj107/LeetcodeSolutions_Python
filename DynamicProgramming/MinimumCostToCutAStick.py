#Approach-1
#Recursive-Approach
#Less Efficient

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def dp(l, r):
            if (l, r) not in memo:
                memo[l, r] = min([dp(l, cut) + dp(cut, r) + (r - l) for cut in cuts if l < cut < r] or [0])
            return memo[l, r]
        return dp(0, n)





#Approach-2
#Efficient

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        sorted_cuts = sorted(cuts + [0, n])
        dp = [[0]*len(sorted_cuts) for _ in range(len(sorted_cuts))]
        for l in range(2, len(sorted_cuts)):
            for i in range(len(sorted_cuts)-l):
                dp[i][i+l] = min(dp[i][j]+dp[j][i+l] for j in range(i+1, i+l)) + \
                             sorted_cuts[i+l]-sorted_cuts[i]
        return dp[0][len(sorted_cuts)-1]

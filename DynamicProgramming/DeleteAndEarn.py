# Approach-1

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        refDict = Counter(nums)
        n = max(nums) + 1
        dp = [0 for _ in range(n)]
        dp[0] = refDict.get(0, 0)
        dp[1] = max(refDict.get(0, 0), refDict.get(1, 0))

        for i in range(2, n):
            dp[i] = max(i * refDict.get(i, 0) + dp[i-2], dp[i-1])

        return dp[n-1]


# Approach-2

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        refDict = Counter(nums)
        prev = refDict.get(0, 0)
        curr = refDict.get(1, 0)

        for i in range(2, max(refDict.keys())+1):
            prev, curr = curr, max(prev + i * refDict.get(i, 0), curr)

        return curr

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num = [0]*(max(nums)+1)
        for i in nums:
            num[i] += i
        dp = [0]*len(num)
        if len(num) == 1:
            return num[0]
        dp[0] = num[0]
        dp[1] = max(num[0], num[1])
        for i in range(2, len(num)):
            dp[i] = max(dp[i-2]+num[i], dp[i-1])
        return dp[-1]

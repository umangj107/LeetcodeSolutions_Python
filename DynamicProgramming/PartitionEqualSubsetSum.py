# Approach-1
# Slower Approach

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetSum(nums, n, target):
            dp = [[False for _ in range(target+1)] for _ in range(n + 1)]
            for i in range(n+1):
                dp[i][0] = True
            for i in range(1, n+1):
                for j in range(1, target+1):
                    if nums[i-1] <= target:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[n][target]

        targetSum = sum(nums)
        if targetSum % 2 != 0:
            return False
        else:
            return subsetSum(nums, len(nums), targetSum//2)


# Approach-2
# Faster Approach

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)):
            nextdp = set()
            for j in dp:
                if (j+nums[i]) == target:
                    return True
                nextdp.add(j + nums[i])
                nextdp.add(j)
            dp = nextdp

        return True if target in dp else False

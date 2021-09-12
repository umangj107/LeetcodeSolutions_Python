# Approach-1

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        else:
            dp = [0 for _ in range(n)]
            ans = 0
            for i in range(2, n):
                if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                    dp[i] = dp[i-1] + 1
                ans += dp[i]
            return ans


# Approach-2
# Optimized Approach

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        else:
            prev = 0
            dp_prev = 0
            ans = 0
            for i in range(2, n):
                if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                    dp_prev = prev + 1
                ans += dp_prev
                prev = dp_prev
                dp_prev = 0
            return ans

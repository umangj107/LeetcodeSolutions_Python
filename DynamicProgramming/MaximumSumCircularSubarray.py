class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        s = sum(nums)
        n = len(nums)

        # Finding max sum of normal array using Kadane's algo
        max_normal = nums[0]
        curr_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_normal = max(max_normal, curr_sum)

        # Inverting each element of array
        nums = [(-1 * i) for i in nums]

        # Finding max sum of inverted array using Kadane's algo
        max_inverted = nums[0]
        curr_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_inverted = max(max_inverted, curr_sum)

        max_inverted = s - (-1 * max_inverted)

        # Returning result
        return max(max_normal, max_inverted)

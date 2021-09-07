class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_overall = nums[0]

        for i in range(1, len(nums)):
            temp = max_so_far
            max_so_far = max([nums[i], nums[i]*max_so_far, nums[i]*min_so_far])
            min_so_far = min([nums[i], nums[i]*temp, nums[i]*min_so_far])
            max_overall = max(max_overall, max_so_far)

        return max_overall

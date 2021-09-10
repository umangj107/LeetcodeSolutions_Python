class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ref = {0: 1}
        count = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            count += ref.get(curr_sum - k, 0)
            ref[curr_sum] = ref.get(curr_sum, 0) + 1

        return count

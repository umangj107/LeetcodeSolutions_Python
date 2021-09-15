class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        local_ones = 0
        for num in nums:
            if num == 1:
                local_ones += 1
            else:
                ones = max(ones, local_ones)
                local_ones = 0

        if(local_ones > ones):
            ones = local_ones
        return ones

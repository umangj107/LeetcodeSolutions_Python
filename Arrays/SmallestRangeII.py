class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            temp_min = min(nums[0]+k, nums[i+1]-k)
            temp_max = max(nums[i]+k, nums[-1]-k)
            res = min(res, (temp_max-temp_min))
            
        return res

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        else:
            n = len(nums)
            nums.sort()
            S=[]

            for k in range(4):
                for j in range(4-k):
                    S.append( nums[n-1-j]-nums[k]  )

            return min(S)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums[:]]
        else:
            res = []
            for i in range(len(nums)):
                x = nums.pop(0)
                p = self.permuteUnique(nums)
                for i in p:
                    i.append(x)
                    if i not in res:
                        res.append(i)
                nums.append(x)

            return res

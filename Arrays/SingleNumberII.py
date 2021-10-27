# Approach-1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        B = [0]*32
        res = 0
        for i in range(32):
            for j in range(len(nums)):
                B[i] += abs(nums[j]) >> i & 1
        for i in range(32):
            if B[i] % 3 != 0:
                res += 1 << i

        return res if nums.count(res) == 1 else -res


# Approach-2
# Faster

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums))-sum(nums))//2

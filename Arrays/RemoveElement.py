# Approach-1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            i = 0
            while i < len(nums):
                if nums[i] == val:
                    nums.pop(i)
                else:
                    i += 1

            return len(nums)


# Approach-2
# Efficient Approach

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

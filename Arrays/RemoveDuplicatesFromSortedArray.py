# Approach-1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            i = 0
            while i < len(nums)-1:
                while i < len(nums)-1 and nums[i+1] == nums[i]:
                    nums.pop(i+1)
                i += 1

            return len(nums)


# Approach-2
# Efficient-Approach

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 0
        for k in range(1, len(nums)):
            if nums[k] > nums[i]:
                nums[i+1], nums[k] = nums[k], nums[i+1]
                i += 1
        return i+1

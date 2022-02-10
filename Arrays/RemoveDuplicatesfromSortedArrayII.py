# Approach-1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        currCount = 1
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                if currCount == 2:
                    nums.pop(index)
                else:
                    currCount += 1
                    index += 1
            else:
                currCount = 1
                index += 1

        return len(nums)


# Approach-2

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        s = 2
        for f in range(2, len(nums)):
            if nums[f] != nums[s-2]:
                nums[s] = nums[f]
                s += 1
        return s

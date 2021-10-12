class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums)-1
        while index > 0:
            if nums[index-1] < nums[index]:
                break
            index -= 1

        if index == 0:
            nums.reverse()
        else:
            nextGreater = index
            for i in range(index, len(nums)):
                if nums[i] > nums[index-1] and nums[i] <= nums[nextGreater]:
                    nextGreater = i
            nums[index-1], nums[nextGreater] = nums[nextGreater], nums[index-1]
            l = index
            r = len(nums)-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            print(nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start = 0
        end = len(nums)-1
        if nums[end] > nums[start]:
            return nums[start]

        while start <= end:
            mid = start + ((end - start)//2)
            nextele = (mid + 1) % n
            prevele = (mid + n - 1) % n
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[0] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

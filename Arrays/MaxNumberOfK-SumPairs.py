# Approach-1

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums)-1

        while left < right:
            s = nums[left] + nums[right]
            if s < k:
                left += 1
            elif s > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

        return count


# Approach-2

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        refDict = Counter(nums)
        count = 0

        for key in refDict:
            otherValue = k-key
            if key == otherValue:
                count += refDict[key] // 2
            elif key < otherValue:
                count += min(refDict[key], refDict[otherValue])

        return count

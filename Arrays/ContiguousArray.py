class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0
        refDict = {0:-1}
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in refDict:
                maxLen = max(maxLen, i - refDict[count])
            else:
                refDict[count] = i
                
        return maxLen
        
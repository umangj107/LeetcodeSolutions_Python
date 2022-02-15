class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        refDict = Counter(nums)
        count = 0

        if k == 0:
            for key, val in refDict.items():
                if val >= 2:
                    count += 1
        else:
            for key, val in refDict.items():
                if key + k in refDict:
                    count += 1
        return count

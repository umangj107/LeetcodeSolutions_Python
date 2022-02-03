# Approach-1

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        refDict12 = {}
        refDict34 = {}

        for i in nums1:
            for j in nums2:
                refDict12[i+j] = refDict12.get(i+j, 0) + 1
        for i in nums3:
            for j in nums4:
                refDict34[i+j] = refDict34.get(i+j, 0) + 1

        count = 0
        for (key, val) in refDict12.items():
            count += refDict34.get(-key, 0) * val

        return count


# Approach-2

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        refDict = {}
        for i in nums1:
            for j in nums2:
                refDict[i+j] = refDict.get(i+j, 0) + 1

        count = 0
        for i in nums3:
            for j in nums4:
                count += refDict.get(-(i+j), 0)

        return count

from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_count = Counter(nums1)
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        nums1_count = self.nums1_count
        nums2_count = self.nums2_count
        n = 0
        for i in nums1_count:
            if tot-i in nums2_count:
                n += nums1_count[i] * nums2_count[tot-i]
        return n

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        nums.clear()
        
        if 0 in counts:
            nums.extend([0 for _ in range(counts[0])])
        if 1 in counts:
            nums.extend([1 for _ in range(counts[1])])
        if 2 in counts:
            nums.extend([2 for _ in range(counts[2])])

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hset = set()
        for num in nums:
            if num in hset:
                hset.remove(num)
            else:
                hset.add(num)
        return list(hset)

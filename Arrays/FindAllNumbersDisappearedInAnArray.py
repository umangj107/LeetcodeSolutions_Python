class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        buffer = [0] * (n+1)
        
        for i in nums:
            buffer[i] += 1
            
        res = []
        for i in range(1, n+1):
            if buffer[i] == 0:
                res.append(i)
        
        return res
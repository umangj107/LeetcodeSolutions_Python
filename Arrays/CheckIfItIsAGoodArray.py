class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if nums == [1]:
            return True
        g = nums[0]
        for i in range(1, len(nums)):

            # g = gcd(g,nums[i])  using gcd() function
            g = self.gcdv(g, nums[i])
            if g == 1:
                return True
        return False

    def gcdv(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcdv(b, a % b)

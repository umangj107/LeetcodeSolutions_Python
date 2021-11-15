# Approach-1

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # Empty set to start the smallest subset.
        # `-1` since anything is divisible by it.
        divisors = {-1: set()}
        for x in nums:
            divisible = []
            for d, subset in divisors.items():
                # Only need to check the key since every
                # other number in the value will be a divisor
                # of the key.
                if x % d == 0:
                    divisible.append(subset)
            # Need to use `.union()` because it will return a new set.
            # Compared to `.add(), which will mutate the set and return `None`.
            divisors[x] = max(divisible, key=len).union({x})
        largest = max(list(divisors.values()), key=len)
        return largest


# Approach-2

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = [[]]
        for i in sorted(nums):
            temp = []
            for j in res:
                if not j or i % j[-1] == 0:
                    temp.append(j + [i])
            res.append(max(temp, key=len))
        return max(res, key=len)

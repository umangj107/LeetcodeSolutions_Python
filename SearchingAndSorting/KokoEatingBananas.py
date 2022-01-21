# Approach-1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            currSpeed = (minSpeed + maxSpeed) // 2
            hoursSpent = 0

            for pile in piles:
                hoursSpent += math.ceil(pile / currSpeed)

            if hoursSpent <= h:
                maxSpeed = currSpeed
            else:
                minSpeed = currSpeed + 1

        return maxSpeed


# Approach-2
# Faster Approach

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)

        s = sum(piles)
        l, r = (s - 1) // h + 1, (s - 1) // (h - len(piles)) + 1

        def isViable(cap):
            return sum((p-1)//cap + 1 for p in piles) <= h
        while l < r:

            m = (l + r) // 2
            if isViable(m):
                r = m
            else:
                l = m + 1
        return l

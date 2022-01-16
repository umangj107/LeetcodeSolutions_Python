class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = 0
        currMax = 0
        lastOne = -1

        for i in seats:
            if i == 0:
                currMax += 1
            else:
                if lastOne == -1:
                    maxDistance = max(maxDistance, currMax)
                else:
                    maxDistance = max(maxDistance, ceil(currMax/2))
                currMax = 0
                lastOne = 0

        return max(maxDistance, currMax)

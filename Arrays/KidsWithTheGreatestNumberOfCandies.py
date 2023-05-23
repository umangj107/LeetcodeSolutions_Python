class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxElement = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= maxElement
        return candies

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        max_prev = values[0] + 0
        for i in range(1, len(values)):
            res = max(res, max_prev + (values[i] - i))
            max_prev = max(max_prev, values[i]+i)

        return res

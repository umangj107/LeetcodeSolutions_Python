import heapq
import math


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        mini = math.inf
        diff = math.inf
        for i in nums:
            if i % 2 != 0:
                i *= 2
            mini = min(mini, i)
            heap.append(-1 * i)

        heapq.heapify(heap)
        while True:
            x = -1 * heapq.heappop(heap)
            diff = min(diff, abs(x - mini))
            if x % 2 != 0:
                break
            else:
                x = (x // 2) * -1
                mini = min(mini, -1 * x)
                heapq.heappush(heap, x)

        return diff

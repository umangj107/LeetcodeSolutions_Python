class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []

        i = 0
        j = 0

        while j < k:
            while queue and queue[-1] < nums[j]:
                queue.pop(-1)
            queue.append(nums[j])
            j += 1

        res = [queue[0]]

        while j < len(nums):
            if queue and nums[i] == queue[0]:
                queue.pop(0)
            while queue and queue[-1] < nums[j]:
                queue.pop(-1)
            queue.append(nums[j])
            res.append(queue[0])

            i += 1
            j += 1

        return res

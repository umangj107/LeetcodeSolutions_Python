# Approach-1

from heapq import heapify, heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = []
        for i in range(len(nums)):
            if stack and nums[i] > stack[-1]:
                temp = []
                while stack and stack[-1] < nums[i]:
                    temp.append(stack.pop(-1))

                stack.append(nums[i])
                while temp:
                    stack.append(temp.pop(-1))
                temp = []

            else:
                stack.append(nums[i])

            if len(stack) > k:
                while len(stack) != k:
                    stack.pop(-1)

        return stack[-1]


# Approach-2
# Using python in-built max-heap module called "heapq"
# Efficient Approach


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums)-k):
            x = heappop(nums)

        return heappop(nums)

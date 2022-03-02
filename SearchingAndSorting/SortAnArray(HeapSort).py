class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(nums, n, i):
            largest = i
            L = 2 * largest + 1
            R = 2 * largest + 2

            if 0 <= L < n and nums[L] > nums[largest]:
                largest = L

            if 0 <= R < n and nums[R] > nums[largest]:
                largest = R

            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(nums, n, largest)

        def heapsort(nums):
            n = len(nums)
            lastNonLeaf = (n // 2) - 1
            for i in range(lastNonLeaf, -1, -1):
                heapify(nums, n, i)

            for i in range(n-1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)

        heapsort(nums)
        return nums

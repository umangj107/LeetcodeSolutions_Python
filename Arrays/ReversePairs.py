class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, l, m, r):
            cnt = 0
            j = m + 1
            for i in range(l, m+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (m+1)

            arr = []
            left = l
            right = m + 1
            while left <= m and right <= r:
                if nums[left] <= nums[right]:
                    arr.append(nums[left])
                    left += 1
                else:
                    arr.append(nums[right])
                    right += 1

            while left <= m:
                arr.append(nums[left])
                left += 1
            while right <= r:
                arr.append(nums[right])
                right += 1

            for i in range(l, r+1):
                nums[i] = arr[i - l]

            return cnt

        def mergeSort(nums, left, right):
            if left >= right:
                return 0
            invCount = 0
            mid = (left + right) // 2
            invCount = mergeSort(nums, left, mid)
            invCount += mergeSort(nums, mid+1, right)
            invCount += merge(nums, left, mid, right)
            return invCount

        return mergeSort(nums, 0, len(nums)-1)

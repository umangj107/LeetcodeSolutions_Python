# Approach-1
# Gives TLE

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_len = 0
        for k in range(len(nums)):
            index = k
            temp = set()
            while index < len(nums):
                if nums[index] in temp:
                    break
                else:
                    temp.add(nums[index])
                    index = nums[index]

            max_len = max(max_len, len(temp))

        return max_len


# Approach-2
# Accepted

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_len = 0
        visited = [False for _ in range(len(nums))]
        for i in range(len(nums)):
            if not visited[i]:
                start = nums[nums[i]]
                count = 1
                while start != nums[i]:
                    start = nums[start]
                    count += 1
                    visited[start] = True
                max_len = max(max_len, count)

        return max_len

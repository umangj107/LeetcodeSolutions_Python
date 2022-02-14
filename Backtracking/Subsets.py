# Approach-1

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]
        return output


# Approach-2
# Backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(lst, start):
            result.append(list(lst))
            for i in range(start, len(nums)):
                lst.append(nums[i])
                backtrack(lst, i+1)
                lst.pop()

        backtrack([], 0)
        return result

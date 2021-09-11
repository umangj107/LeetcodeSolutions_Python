# Approach-1

class Solution:
    def __init__(self):
        self.result = []

    def backtracking(self, nums, curr_list, visited, n):
        if len(curr_list) == len(nums):
            self.result.append(list(curr_list))
            print(self.result)
            return
        else:
            for i in range(n):
                if visited[i]:
                    continue
                else:
                    curr_list.append(nums[i])
                    visited[i] = True
                    self.backtracking(nums, curr_list, visited, n)
                    curr_list.pop(-1)
                    visited[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_list = []
        visited = [False for _ in range(len(nums))]
        n = len(nums)
        self.backtracking(nums, curr_list, visited, n)
        return self.result


# Approach-2


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums[:]]
        else:
            res = []
            for i in range(len(nums)):
                x = nums.pop(0)
                perms = self.permute(nums)
                for i in perms:
                    i.append(x)
                res += perms
                nums.append(x)

        return res

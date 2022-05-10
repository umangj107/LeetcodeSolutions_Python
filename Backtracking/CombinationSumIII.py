class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []

        def dfs(path, k, n, arr):
            if k < 0 or n < 0:
                return
            elif k == 0 and n == 0:
                self.res.append(path)
                return
            else:
                for i in range(len(arr)):
                    dfs(path+[arr[i]], k-1, n-arr[i], arr[i+1:])

        dfs([], k, n, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        return self.res

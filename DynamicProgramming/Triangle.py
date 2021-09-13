# Approach-1
# Recursive Approach

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @lru_cache(None)
        def helper(row, col):
            if row == n:
                return 0
            elif col < 0 or col >= len(triangle[row]):
                return 99999
            return triangle[row][col] + min(helper(row+1, col), helper(row+1, col+1))

        return helper(0, 0)


# Approach-2

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

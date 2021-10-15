# Approach-1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1

        while row < m and matrix[row][col] < target:
            row += 1

        while row < m and col < n and row >= 0 and col >= 0:
            while col >= 0 and matrix[row][col] > target:
                col -= 1
            if col < 0:
                return False

            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                return False

        return False


# Approach-2

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.found = False

        def binary_search(arr, left, right, val):
            if left <= right:
                pivot_index = (left+right)//2
                pivot = arr[pivot_index]
                if pivot == val:
                    self.found = True
                    return
                if pivot < val:
                    binary_search(arr, pivot_index+1, right, val)
                else:
                    binary_search(arr, left, pivot_index-1, val)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            binary_search(matrix[i], 0, n-1, target)
            if self.found:
                return True
            self.found = False
        return False

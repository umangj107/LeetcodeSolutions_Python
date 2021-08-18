#Approach-1
#Using Binary Search over row and column

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_row(matrix, target):
            start = 0
            end = len(matrix)
            while start <= end:
                mid = (start+end)//2
                if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                    return mid
                elif matrix[mid][0] > target:
                    end = mid-1
                elif matrix[mid][-1] < target:
                    start = mid+1
                    
            return -1
        
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row_index = get_row(matrix, target)
        if row_index == -1:
            return False
        row = matrix[row_index]
        start = 0
        end = len(row)
        while start <= end:
            mid = (start+end)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid+1
            elif row[mid] > target:
                end = mid-1
                
        return False
      
     
#Approach-2
#Efficient Approach

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        row = 0
        col = len(matrix[0])-1
        
        while row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row+=1
            else:
                break
                
        while col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col-=1
            else:
                return False

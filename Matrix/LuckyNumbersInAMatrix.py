class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        colRes = []
        n = len(matrix)
        m = len(matrix[0])
        result = []
        
        for j in range(m):
            colMax = 0
            for i in range(n):
                if matrix[i][j] > colMax:
                    colMax = matrix[i][j]
            colRes.append(colMax)
            
        for i in range(n):
            rowMin = matrix[i][0]
            for j in range(m):
                if matrix[i][j] < rowMin:
                    rowMin = matrix[i][j]
            if rowMin in colRes:
                result.append(rowMin)
            
        return result
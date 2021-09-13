class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 1:
            return [[1]]
        result = [[1] for _ in range(numRows)]
        result[0] = [1]
        result[1] = [1, 1]

        for i in range(2, numRows):
            for j in range(1, len(result[i-1])):
                x = result[i-1][j]
                if j-1 >= 0:
                    y = result[i-1][j-1]
                result[i].append(x+y)
            result[i].append(1)
        return result

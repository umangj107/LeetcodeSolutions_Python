class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        refDict = {}
        for i in range(len(mat) + len(mat[0])):
            refDict[i] = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                refDict[i+j].insert(0, mat[i][j])

        result = []
        for key in refDict.keys():
            x = refDict[key]
            if key % 2 != 0:
                x = x[::-1]
            result += x

        return result

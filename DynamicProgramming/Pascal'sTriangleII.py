class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        else:
            prev = [1, 1]
            curr = [1]

            for k in range(2, rowIndex+1):
                for i in range(1, len(prev)):
                    curr.append(prev[i] + prev[i-1])
                curr.append(1)
                print(curr)
                prev = curr
                curr = [1]

            return prev

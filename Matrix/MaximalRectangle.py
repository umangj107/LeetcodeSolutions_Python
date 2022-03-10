class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_NSL(arr):
            res = []
            stack = []
            for i in range(len(arr)):
                if not stack:
                    res.append(-1)
                elif stack and stack[-1][0] < arr[i]:
                    res.append(stack[-1][1])
                elif stack and stack[-1][0] >= arr[i]:
                    while stack and stack[-1][0] >= arr[i]:
                        stack.pop(-1)
                    if not stack:
                        res.append(-1)
                    else:
                        res.append(stack[-1][1])

                stack.append((arr[i], i))

            return res

        def get_NSR(arr):
            res = []
            stack = []
            for i in range(len(arr)-1, -1, -1):
                if not stack:
                    res.append(len(arr))
                elif stack and stack[-1][0] < arr[i]:
                    res.append(stack[-1][1])
                elif stack and stack[-1][0] >= arr[i]:
                    while stack and stack[-1][0] >= arr[i]:
                        stack.pop(-1)
                    if not stack:
                        res.append(len(arr))
                    else:
                        res.append(stack[-1][1])

                stack.append((arr[i], i))

            return res[::-1]

        def MAH(arr):
            n = len(arr)
            NSL = get_NSL(arr)
            NSR = get_NSR(arr)

            max_area = 0
            for i in range(n):
                area = (NSR[i] - NSL[i] - 1) * arr[i]
                max_area = max(area, max_area)
            return max_area

        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        temp = [int(x) for x in matrix[0]]
        result = max(result, MAH(temp))
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    temp[c] = 0
                else:
                    temp[c] += 1
            result = max(result, MAH(temp))
        return result

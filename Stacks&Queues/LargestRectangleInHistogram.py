class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.NSL = []
        self.NSR = []

        def get_NSL(heights):
            index = 0
            stack = []

            for i in range(len(heights)):
                if not stack:
                    self.NSL.append(-1)
                elif stack and stack[-1][0] < heights[i]:
                    self.NSL.append(stack[-1][1])
                elif stack and stack[-1][0] >= heights[i]:
                    while stack and stack[-1][0] >= heights[i]:
                        stack.pop(-1)
                    if not stack:
                        self.NSL.append(-1)
                    else:
                        self.NSL.append(stack[-1][1])

                stack.append((heights[i], i))

        def get_NSR(heights):
            stack = []
            for i in range(len(heights)-1, -1, -1):
                if not stack:
                    self.NSR.append(len(heights))
                elif stack and stack[-1][0] < heights[i]:
                    self.NSR.append(stack[-1][1])
                elif stack and stack[-1][0] >= heights[i]:
                    while stack and stack[-1][0] >= heights[i]:
                        stack.pop(-1)
                    if not stack:
                        self.NSR.append(len(heights))
                    else:
                        self.NSR.append(stack[-1][1])

                stack.append((heights[i], i))

        get_NSL(heights)
        get_NSR(heights)
        self.NSR = self.NSR[::-1]
        max_area = 0
        for i in range(len(heights)):
            r = self.NSR[i]
            l = self.NSL[i]
            area = (r-l-1) * heights[i]
            max_area = max(area, max_area)

        return max_area

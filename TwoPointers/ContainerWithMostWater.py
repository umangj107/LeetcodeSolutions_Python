class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0  # first (left) pointer
        p2 = len(height) - 1  # second (right) pointer
        max_area = 0
        while p1 != p2:
            if height[p1] > height[p2]:
                # height of smaller edge multiplies on length
                area = height[p2] * (p2 - p1)
                p2 -= 1  # changing smaller edge
            else:
                area = height[p1] * (p2 - p1)
                p1 += 1
            if area > max_area:
                max_area = area  # increasing max area if possible
        return max_area

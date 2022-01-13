class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        lastArrowPos = points[0][1]
        arrowCount = 1

        for point in points:
            if point[0] <= lastArrowPos:
                continue
            else:
                lastArrowPos = point[1]
                arrowCount += 1

        return arrowCount

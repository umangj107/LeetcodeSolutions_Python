class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 1 and capacity < trips[0][0]:
            return False

        trips = sorted(trips, key=lambda x: x[1])

        refDict = {}
        for trip in trips:
            refDict[trip[1]] = refDict.get(trip[1], 0) + trip[0]
            refDict[trip[2]] = refDict.get(trip[2], 0) - trip[0]

        currPassengers = 0
        for i in sorted(refDict.keys()):
            currPassengers += refDict[i]
            if currPassengers > capacity:
                return False

        return True

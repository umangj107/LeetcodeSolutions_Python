class UndergroundSystem:

    def __init__(self):
        self.checkedInIds = dict()
        self.avgTimes = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedInIds.keys():
            self.checkedInIds[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedInIds.keys():
            x = self.checkedInIds[id]
            self.checkedInIds.pop(id)
            newEntry = self.avgTimes.get((x[0], stationName), [0, 0])
            newEntry[0] += (t - x[1])
            newEntry[1] += 1
            self.avgTimes[(x[0], stationName)] = newEntry

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        reqEntry = self.avgTimes.get((startStation, endStation), [0, 0])
        return reqEntry[0] / reqEntry[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

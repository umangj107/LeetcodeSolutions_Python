class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        drinkBottles = numBottles
        
        while emptyBottles >= numExchange:
            exchanges = emptyBottles // numExchange
            drinkBottles += exchanges
            emptyBottles = emptyBottles + exchanges - (exchanges * numExchange)
        
        return drinkBottles
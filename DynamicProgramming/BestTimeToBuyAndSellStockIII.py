class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pfst = [0] * n
        profit = 0

        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            pfst[i] = max(pfst[i-1], prices[i]-minPrice)

        maxPrice = prices[n-1]
        for i in range(n-1, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            pfbt = maxPrice - prices[i]
            profit = max(profit, pfst[i]+pfbt)

        return profit

# Approach-1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        i = 0
        max_profit = 0
        while i < n:
            buy = 0
            sell = 0
            while i < n-1 and prices[i+1] < prices[i]:
                i += 1
            buy = prices[i]
            while i < n-1 and prices[i+1] > prices[i]:
                i += 1
            sell = prices[i]

            max_profit += (sell - buy)
            i += 1
        return max_profit


# Approach-2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i-1], 0)

        return max_profit

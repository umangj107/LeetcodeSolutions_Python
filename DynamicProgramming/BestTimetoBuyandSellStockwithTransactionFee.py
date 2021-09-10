# Approach-1

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        bought_state = -1 * prices[0]
        sold_state = 0

        for i in range(1, n):
            bought_state = max(bought_state, sold_state - prices[i])
            sold_state = max(sold_state, bought_state + prices[i] - fee)

        return sold_state


# Approach-2

class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans

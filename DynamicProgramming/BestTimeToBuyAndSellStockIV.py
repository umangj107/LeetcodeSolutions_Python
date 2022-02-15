class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        buys = [9999] * k
        sells = [-9999] * k

        for i in range(n):
            for j in range(k):
                if j == 0:
                    buys[j] = min(buys[0], prices[i])
                    sells[j] = max(sells[0], prices[i]-buys[0])
                else:
                    buys[j] = min(buys[j], prices[i]-sells[j-1])
                    sells[j] = max(sells[j], prices[i]-buys[j])

        return sells[-1]

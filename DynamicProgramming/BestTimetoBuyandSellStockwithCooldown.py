class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def get_max(index, engaged, last_sold):
            if index == len(prices):
                return 0
            else:
                ans = 0
                if engaged:
                    sell = get_max(index+1, 0, 1) + prices[index]
                    skip = get_max(index+1, 1, 0)
                    ans = max(sell, skip)

                else:
                    buy = 0
                    if not last_sold:
                        buy = get_max(index+1, 1, 0) - prices[index]
                    skip = get_max(index+1, 0, 0)
                    ans = max(buy, skip)

                return ans

        return get_max(0, 0, 0)

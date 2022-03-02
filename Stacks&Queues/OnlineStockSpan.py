class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        count = 1
        if not self.span:
            self.span.append([price, count])
            return count

        while self.span:
            curr_ele, curr_cnt = self.span[-1]
            if curr_ele <= price:
                count += curr_cnt
                self.span.pop()
            else:
                self.span.append([price, count])
                return count

        self.span.append([price, count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

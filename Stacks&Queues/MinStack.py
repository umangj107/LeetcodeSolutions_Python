class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_top = -1
        self.min_element = -1

    def push(self, val: int) -> None:
        if self.stack_top == -1:
            self.min_element = val

        elif val < self.min_element:
            temp = (2 * val) - self.min_element
            self.min_element = val
            val = temp

        self.stack_top += 1
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack_top > -1:
            self.stack_top -= 1
            x = self.stack.pop(-1)
            if x < self.min_element:
                self.min_element = (2 * self.min_element) - x

    def top(self) -> int:
        if self.stack[-1] >= self.min_element:
            return self.stack[-1]
        else:
            return self.min_element

    def getMin(self) -> int:
        return self.min_element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

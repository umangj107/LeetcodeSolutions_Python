# Approach-1
# Using extra space

class MinStack:

    def __init__(self):
        self.stack = []
        self._top = -1
        self.MS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._top += 1
        if len(self.MS) == 0 or val <= self.MS[-1]:
            self.MS.append(val)

    def pop(self) -> None:
        x = self.stack.pop(-1)
        self._top -= 1
        if self.MS and self.MS[-1] == x:
            self.MS.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self._top == -1:
            return -1
        return self.MS[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Approach-2
# With O(1) space


class MinStack:

    def __init__(self):
        self.stack = []
        self._top = -1
        self.curr_min = -1

    def push(self, val: int) -> None:
        x = val
        if self._top == -1:
            self.curr_min = val
            x = val
        elif self.curr_min >= val:
            x = (2 * val) - self.curr_min
            self.curr_min = val
        self.stack.append(x)
        self._top += 1

    def pop(self) -> None:
        if self._top > -1:
            x = self.stack.pop(-1)
            self._top -= 1

            if x < self.curr_min:
                self.curr_min = (2 * self.curr_min) - x

    def top(self) -> int:
        if self.stack[-1] >= self.curr_min:
            return self.stack[-1]
        else:
            return self.curr_min

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

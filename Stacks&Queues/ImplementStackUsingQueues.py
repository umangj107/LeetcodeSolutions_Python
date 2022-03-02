# Approach-1
# Using two queues

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.empty():
            self.q2 = []
            for i in range(len(self.q1)-1):
                self.q2.append(self.q1.pop(0))
            x = self.q1.pop(0)
            self.q1 = self.q2
            return x

        return -1

    def top(self) -> int:
        if not self.empty():
            return self.q1[-1]
        return -1

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Approach-2
# Using Single Queue

class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.empty():
            n = len(self.q)
            for i in range(n-1):
                self.q.append(self.q.pop(0))
            return self.q.pop(0)
        return -1

    def top(self) -> int:
        if not self.empty():
            return self.q[-1]
        return -1

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

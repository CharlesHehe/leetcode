from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop(-1)

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(item for item in self.items)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
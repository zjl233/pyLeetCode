from typing import List


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums: List[int] = []
        self.mins: List[int] = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.mins and x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        n = self.nums.pop()
        if n == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

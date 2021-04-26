#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#


# @lc code=start
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.capacity:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == len(self.stack):
                break

            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # each element would be a pair of (x, current_min)
        self._stack = []
        

    def push(self, x: int) -> None:
        if not self._stack:
            self._stack.append([x, x])
        else:
            self._stack.append([x, min(self._stack[-1][1], x)])

    def pop(self) -> None:
        return self._stack.pop()[0]
        

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


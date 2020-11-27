#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        # Stack 用来存list of tuples, 其中一个tuple是(price, count).
        # 这里count指的是在这个price之前比它小的天数。
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        # 如果栈顶的tuple的price比当前price小，就出栈。
        # 计算一下比这个price小的天数有多少，然后将当前price做
        # 入栈。这里比较巧的是count能够储存刚刚被出栈的元素的信息，
        # 所以我们不需要保存了。
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end


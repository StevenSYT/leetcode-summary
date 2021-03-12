#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#


# @lc code=start
class MyCalendarThree:
    def __init__(self):
        self.points = []

    def book(self, start: int, end: int) -> int:
        self.points.append((start, 1))
        self.points.append((end, -1))
        self.points.sort()

        cnt = 0
        res = 0
        for point in self.points:
            cnt += point[1]
            res = max(cnt, res)

        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end

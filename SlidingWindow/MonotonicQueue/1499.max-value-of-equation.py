#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        res = float('-inf')
        # We need to analyze the equation first:
        # yi + yj + |xi - xj| = (yi - xi) + xj + yj
        # note that xi < xj and i < j.
        # Then the problem becomes: for each new point p, maintain
        # the largest (ym - xm) in the current window for p.
        # also note that(xp - xm) <= k.
        for x, y in points:
            while q and x - q[0][0] > k:
                q.popleft()
            if q:
                res = max(res, q[0][1] + x + y)
            while q and q[-1][1] < y - x:
                q.pop()
            q.append((x, y - x))
        return res


# @lc code=end

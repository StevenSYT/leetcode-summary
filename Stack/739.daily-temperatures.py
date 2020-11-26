#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        warm_days = [0] * n
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                day_idx = stack.pop()
                warm_days[day_idx] = i - day_idx
            stack.append(i)
        return warm_days
# @lc code=end


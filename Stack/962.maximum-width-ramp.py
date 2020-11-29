#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#


# @lc code=start
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # 先用一个单调严格递减栈从左往右遍历压栈
        stack = []
        n = len(A)
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        res = 0
        # 然后从右往左遍历，找到对每个元素最远的最小元素
        for j in range(n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[j]:
                i = stack.pop()
            res = max(res, j - i)
        return res


# @lc code=end

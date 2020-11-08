#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#


# @lc code=start
# stack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]

        for num in arr:
            # push the numbers in stack
            # if the new number (num) is larger than the top one
            # in the stack (mid), remove the number at top of the
            # stack with cost of mid multiple the smaller one of its
            # adjacent numbers.
            while stack[-1] <= num:
                mid = stack.pop()
                # num is the right side of mid, and stack[-1] is the left
                # side of the mid
                res += mid * min(num, stack[-1])
            stack.append(num)
        # After the for loop, the numbers stored in the stack are sorted
        # with top of the stack the smallest one.
        # Pop stack until only 'inf' and the largest value left
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


# DP
class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for d in range(1, n):
            for left in range(0, n - d):
                right = left + d
                dp[left][right] = min([
                    dp[left][k] + dp[k + 1][right] +
                    max(arr[left:k + 1]) * max(arr[k + 1:right + 1])
                    for k in range(left, right)
                ])
        return dp[0][n - 1]

# Recursion with memo
class Solution3:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.dfs(arr, 0, len(arr) - 1, {})

    # dp[left][right] is the Minimum Cost Tree From Leaf Values between left and right inclusive.
    def dfs(self, arr, left, right, cache):
        if left >= right: return 0

        if (left, right) in cache:
            return cache[left, right]

        cache[left, right] = min([
            self.dfs(arr, left, k, cache) +
            self.dfs(arr, k + 1, right, cache) +
            max(arr[left:k + 1]) * max(arr[k + 1:right + 1])
            for k in range(left, right)
        ])

        return cache[left, right]


# @lc code=end

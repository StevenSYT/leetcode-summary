#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

        for end in range(1, n + 1): # end from 1 ~ n
            # Start from 1 ~ end and in reverse order.
            # This way we can perform a bottom-up dp.
            for start in range(end, 0, -1): 
                if start == end:
                    dp[start][end] = 0
                if start + 1 == end:
                    dp[start][end] = start
                else:
                    for x in range(start + 1, end):
                        dp[start][end] = min(dp[start][end], max(dp[start][x - 1], dp[x + 1][end]) + x)
        return dp[1][n]
        
# @lc code=end


#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#

# @lc code=start
import math
class Solution:
    # 这道题用DP解更快，赢得思路很简单，只要这轮取了一种范围以内的
    # 绝对平方数，能让对手无法获胜，那自己就胜利了。
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for k in range(1, int(i**0.5) + 1):
                if not dp[i-k**2]:
                    dp[i] = True
                    break
        return dp[n]
# @lc code=end


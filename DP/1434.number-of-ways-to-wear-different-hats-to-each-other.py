#
# @lc app=leetcode id=1434 lang=python3
#
# [1434] Number of Ways to Wear Different Hats to Each Other
#


# @lc code=start
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        N = (1 << n)
        mod = 10**9 + 7

        h_to_p = [[] for _ in range(40)]
        for p in range(n):
            for h in hats[p]:
                h_to_p[h - 1].append(p)

        dp = [0] * N
        dp[0] = 1

        for h in range(40):
            for state in range(N - 1, -1, -1):
                for p in h_to_p[h]:
                    if (state & (1 << p) == 0):
                        dp[state | (1 << p)] = (dp[state |
                                                   (1 << p)] + dp[state]) % mod
        return dp[-1]


# @lc code=end

#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#


# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        #     dp[i][k]: min difficulty to schedule the first i jobs to be finished in k days
        #     Base case: dp[0][0] = 0, dp[*][*] = inf
        #     Transition: dp[i][k] = min: dp[j][k-1] + max difficulty between [j+1~i] where k-1 <= j < i
        #     Meaning: try different first j jobs within k-1 days
        n = len(jobDifficulty)
        if d > n: return -1

        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        # bottom up: need to fill dp[1][1], dp[1][2]
        for i in range(1, n + 1):  # for the first i tasks
            for k in range(1, d + 1):  # for the first k days
                if k > i: break
                # dp[i][k] = min(dp[j][k-1] + difficulty for each j)
                # Reverse order: when j = i - 1, max_diff = jobDifficulty[i]
                max_diff = 0
                for j in range(i - 1, k - 2, -1):
                    max_diff = max(max_diff, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + max_diff)

        return dp[n][d]


# @lc code=end

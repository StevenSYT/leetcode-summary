#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#

# @lc code=start
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        # 这题的思路是从i, j 之间选一个点k然后取三角形i,j,k出来，剩下的部分就是dp[i][k] + dp[k][j]，这样的k里选一个和为最小的。
        # 主要的tricky的地方是选顺序，怎样传递才能保证完全的bottom up
        for j in range(2, n):
            for i in range(j-2, -1, -1):
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        return dp[0][n-1]
# @lc code=end


#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#

# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n + [0]

        # 这类题套路差不多，这题的base case要小心
        # 因为stone value可以是负数
        for i in range(n-1, -1, -1):
            cur_sum = 0
            for j in range(0, 3):
                if i + j >= n: break
                cur_sum += stoneValue[i+j]
                dp[i] = max(dp[i], cur_sum - dp[i + j + 1])
        if dp[0] > 0: return 'Alice'
        elif dp[0] < 0: return 'Bob'
        else: return 'Tie'

        
# @lc code=end


#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1:
                dp[i] = nums[i]
                continue
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n]

        
# @lc code=end


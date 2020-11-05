#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add paddings to nums
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        # dp[left][right] = max coins between (left, right) --- exclusive.
        for d in range(2, n):
            for left in range(0, n - d):
                right = left + d
                # 中间的k代表最后一个被打爆的气球，这样直接转化成三角形那道题了，见1039。本质就是
                # 最后的结果里一定有 left * k * right这个结果，对应三角形那道题里最后结果里一定有i * k * j
                # 这个三角形存在。然后剩下的分成左右两个子问题。
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], 
                                         nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        return dp[0][n-1]
# @lc code=end


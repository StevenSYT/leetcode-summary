#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        l = preSum = 0
        res = n + 1
        for r in range(n):
            preSum += nums[r]
            while preSum >= s:
                res = min(res, r - l + 1)
                preSum -= nums[l]
                l += 1
        return res % (n + 1)


# @lc code=end

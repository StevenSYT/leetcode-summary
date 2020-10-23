#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.get_sum(nums, S, {})
    def get_sum(self, nums, target, cache):
        if ((len(nums), target) in cache): return cache[(len(nums), target)]

        if (len(nums) == 0):
            if (target == 0): return 1
            else: return 0

        count = self.get_sum(nums[:-1], target - nums[-1], cache) \
            + self.get_sum(nums[:-1], target + nums[-1], cache)
        cache[(len(nums), target)] = count
        return count        
# @lc code=end


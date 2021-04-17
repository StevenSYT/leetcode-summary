#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#

# @lc code=start
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        def dfs(nums):
            if len(nums) <= 2: return 1

            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left) + len(right),
                        len(right)) * dfs(left) * dfs(right) % mod

        return dfs(nums) - 1


# @lc code=end

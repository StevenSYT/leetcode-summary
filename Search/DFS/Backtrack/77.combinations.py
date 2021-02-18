#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n + 1)
        res = []
        self.dfs([], nums, k, res)
        return res

    def dfs(self, path, nums, k, res):
        if k == 0:
            res.append(path)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.dfs(path + [nums[i]], nums[i + 1:], k - 1, res)
        
# @lc code=end


#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        if len(path) > 1:
            res.append(path)
        used = set()
        for i in range(pos, len(nums)):
            if nums[i] in used: continue
            if not path or path[-1] <= nums[i]:
                used.add(nums[i])
                self.dfs(nums, i + 1, path + [nums[i]], res)
# @lc code=end


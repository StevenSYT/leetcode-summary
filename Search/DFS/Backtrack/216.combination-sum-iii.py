#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1, 10)
        res = []
        self.dfs([], nums, k, n, res)
        return res

    def dfs(self, path, nums, k, target, res):
        if k == 0:
            if target == 0:
                res.append(path)
            return

        for i in range(len(nums)):
            if nums[i] > target:
                break

            self.dfs(path + [nums[i]], nums[i + 1:], k - 1, target - nums[i],
                     res)


# @lc code=end

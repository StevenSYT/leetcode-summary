#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(candidates)
        res = []
        self.dfs([], sorted_nums, target, res)
        return res
    
    
    def dfs(self, path, nums, target, res):
        if target == 0:
            res.append(path)
            return
        
        if target < 0:
            return
        
        for i in range(len(nums)):
            if nums[i] > target:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.dfs(path + [nums[i]], nums[i:], target - nums[i], res)
# @lc code=end


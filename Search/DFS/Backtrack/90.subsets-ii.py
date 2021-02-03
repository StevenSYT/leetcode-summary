#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        self.dfs([], 0, sorted_nums, res)
        return res
    
    def dfs(self, subset, pos, nums, res):
        res.append(subset.copy())

        for i in range(pos, len(nums)):
            if i > pos and nums[i] == nums[i - 1]:
                continue
            
            subset.append(nums[i])
            self.dfs(subset, i + 1, nums, res)
            # backtrack
            subset.pop()


# @lc code=end


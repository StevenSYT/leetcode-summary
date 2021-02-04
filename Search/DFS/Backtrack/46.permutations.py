#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_sets = set(nums)
        res = []
        self.dfs([], num_sets, res)
        return res
    
    def dfs(self, path, nums, res):
        if not nums:
            res.append(path.copy())
            return
        
        for num in list(nums):
            path.append(num)
            nums.remove(num)
            self.dfs(path, nums, res)
            # Backtrack
            nums.add(num)
            path.pop()



# @lc code=end


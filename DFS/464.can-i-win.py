#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Some fast returns
        # 1. If the total sum of all possible integers is less than the goal,
        # you cannot win.
        max_sum = (1 + maxChoosableInteger) * maxChoosableInteger / 2
        if max_sum < desiredTotal:
            return False
        # 2. If the total sum equals to the desiredTotal and the number of turns
        # is odd number, you can win.
        if max_sum == desiredTotal:
            return maxChoosableInteger % 2
        
        # Slow checking
        nums = list(range(1, maxChoosableInteger + 1))
        cache = {}
        return self.dfs(tuple(nums), desiredTotal, cache)

    def dfs(self, nums, target, cache):
        if (nums, target) in cache:
            return cache[(nums, target)]
        if (nums[-1] >= target):
            return True

        # This is a game, we always want to win, and the opponent also
        # wants to win, so if we find if there is any pick this round that
        # won't get the opponent win, we choose it and mark our victory.
        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i+1:], target - nums[i], cache):
                cache[(nums, target)] = True
                return True
        cache[(nums, target)] = False
        return False
# @lc code=end


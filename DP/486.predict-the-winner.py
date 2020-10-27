#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
# 这道题的思路就是用score()来算当前区间first in action player能比对手最多高多少分
# 巧妙的地方在于score针对的不是某一个player，而是当前要选的人，所以max的逻辑适用，
# 因为双方都想让这个score对自己更高。
# Base case就是当left == right的时候，当前player肯定直接就选这唯一的数字。
# 如果left != right，那就是当前区间有多个数可选，假设当前player是A，次轮是B，
# A要么选left, 要么选right，选left的话，B在次轮能比A多的分数就是
# score(left + 1, right)。选right的话，B在次轮能比A多的分数就是
# score(left, right - 1)。因为score(left, right)是要求对A而言能比对手赢得最多
# 得情况，那么我们就能得出：
# score(left, right) = max(nums[left] - score(left + 1, right), 
#                          nums[right] - score(left, right - 1))
# 以此递归下去就是结果。
# 


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = {}
        return self.score(0, len(nums) - 1, nums, cache) >= 0

    def score(self, left, right, nums, cache):
        if (left, right) not in cache:
            if left == right:
                return nums[left]
            cache[(left, right)] = max(
                nums[left] - self.score(left + 1, right, nums, cache),
                nums[right] - self.score(left, right - 1, nums, cache))
        return cache[(left, right)]


# @lc code=end

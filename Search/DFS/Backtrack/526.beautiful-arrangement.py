#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#


# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))

        return self.dfs([], nums)

    def is_divisible(self, a, b):
        return a // b >= 1 and a % b == 0

    def dfs(self, path, nums):
        if not nums:
            return 1

        res = 0
        i = len(path) + 1

        for idx in range(len(nums)):
            if self.is_divisible(nums[idx], i) or self.is_divisible(
                    i, nums[idx]):
                res += self.dfs(path + [nums[idx]],
                                nums[:idx] + nums[idx + 1:])

        return res


# @lc code=end

#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.dfs(piles, 0, 1, {})
    def dfs(self, piles, left, M, cache):
        n = len(piles)
        if left + 2 * M >= n:
            cache[left, M] = sum(piles[left:])
            return cache[left, M]
        if (left, M) in cache:
            return cache[left, M]

        res = 0
        for x in range(1, 2 * M + 1):
            res = max(res, sum(piles[left:]) - self.dfs(piles, left + x, max(M, x), cache))
        cache[(left, M)] = res
        return res

# @lc code=end


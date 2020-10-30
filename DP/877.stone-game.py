#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# It is the same as 486.

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.helper(0, len(piles) - 1, piles, {})
        
    def helper(self, left, right, piles, cache):
        if left == right:
            return piles[left]
        if (left, right) in cache:
            return cache[left, right]
        cache[left, right] = max(piles[left] - self.helper(left + 1, right, piles, cache),
                                 piles[right] - self.helper(left, right - 1, piles, cache))
        return cache[left, right]        
# @lc code=end


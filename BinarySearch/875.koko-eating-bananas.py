#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.valid(piles, h, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def valid(self, piles, h, k):
        hrs = 0
        for pile in piles:
            hrs += pile // k
            if pile % k != 0:
                hrs += 1

        return hrs <= h
# @lc code=end

#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#


# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low, high = max(weights), sum(weights)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(weights, D, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def is_valid(self, weights, D, cap):
        days = 1
        cum_sum = 0

        for weight in weights:
            if cum_sum + weight > cap:
                cum_sum = 0
                days += 1

            cum_sum += weight

        return days <= D


# @lc code=end

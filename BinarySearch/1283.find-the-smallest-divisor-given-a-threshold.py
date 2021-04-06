#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#


# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.is_valid(nums, threshold, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def is_valid(self, nums, threshold, div):
        return sum(math.ceil(num / div) for num in nums) <= threshold


# @lc code=end

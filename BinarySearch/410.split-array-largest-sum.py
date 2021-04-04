#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#


# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        res = 0
        while low <= high:
            mid = (low + high) // 2

            if self.is_valid(nums, m, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

    def is_valid(self, nums, m, target):
        num_array = 1
        cur_sum = 0

        for num in nums:
            if cur_sum + num <= target:
                cur_sum += num

            else:
                cur_sum = num
                num_array += 1

        return num_array <= m


# @lc code=end

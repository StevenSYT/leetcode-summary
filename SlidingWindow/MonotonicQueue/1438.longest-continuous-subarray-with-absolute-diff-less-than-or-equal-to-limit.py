#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q_max = deque()
        q_min = deque()
        res = 0
        l = 0

        for r, num in enumerate(nums):
            while q_max and nums[q_max[-1]] < num:
                q_max.pop()
            while q_min and nums[q_min[-1]] > num:
                q_min.pop()

            q_max.append(r)
            q_min.append(r)

            while q_max and q_min and nums[q_max[0]] - nums[q_min[0]] > limit:
                if q_max[0] < q_min[0]:
                    l = q_max.popleft() + 1
                if q_min[0] < q_max[0]:
                    l = q_min.popleft() + 1
            res = max(res, r - l + 1)
        return res


# @lc code=end

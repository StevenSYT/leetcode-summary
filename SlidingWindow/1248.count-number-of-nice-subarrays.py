#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            odd_count, res = 0, 0
            l = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2 == 1:
                        odd_count -= 1
                    l += 1
                res += r - l + 1
            return res

        return atMost(k) - atMost(k - 1)


# @lc code=end

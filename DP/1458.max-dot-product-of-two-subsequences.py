#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#


# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return float('-inf')
            product = nums1[i] * nums2[j]
            return max(product, product + dfs(i - 1, j - 1), dfs(i, j - 1),
                       dfs(i - 1, j))
        return dfs(len(nums1) - 1, len(nums2) - 1)


# @lc code=end

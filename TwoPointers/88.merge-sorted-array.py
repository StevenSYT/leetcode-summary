#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        p = m + n - 1
        while p >= 0:
            if p1 < 0:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1


# @lc code=end

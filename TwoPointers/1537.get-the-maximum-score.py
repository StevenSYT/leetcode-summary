#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#


# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = s2 = 0
        p1 = p2 = 0
        m, n = len(nums1), len(nums2)
        mod = 10**9 + 7

        while p1 < m or p2 < n:
            if p1 == m:  # p2 < n, directly move p2
                s2 += nums2[p2]
                p2 += 1

            elif p2 == n:  # p1 < m, directly move p1
                s1 += nums1[p1]
                p1 += 1

            else:  # p1, p2 both haven't reached end
                if nums1[p1] < nums2[p2]:
                    s1 += nums1[p1]
                    p1 += 1

                elif nums2[p2] < nums1[p1]:
                    s2 += nums2[p2]
                    p2 += 1

                else:  # nums2[p2] == nums1[p1]
                    s1 = s2 = max(s1, s2) + nums1[p1]
                    p1 += 1
                    p2 += 1

        return max(s1, s2) % mod


# @lc code=end

#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#


# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # Sliding window, define an function atMost(S) which returns
        # the number of subarrays that sums up to at most S.
        # The exact number of subarrays that sums to S equals to
        # atMost(S) - atMost(S - 1)
        def atMost(S):
            if S < 0:
                return 0
            preSum, res, l = 0, 0, 0
            for r in range(len(A)):
                preSum += A[r]
                while preSum > S:
                    preSum -= A[l]
                    l += 1
                res += r - l + 1
            return res

        return atMost(S) - atMost(S - 1)


# @lc code=end

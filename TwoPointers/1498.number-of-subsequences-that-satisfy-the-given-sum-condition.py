#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#


# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        A = sorted(nums)

        l, r = 0, len(A) - 1
        mod = 10**9 + 7
        res = 0

        while l <= r:
            if A[l] + A[r] > target:
                r -= 1

            else:
                # There are 2 ^ (r - l) subsequences for subarray A[l] ~ A[r]
                # with A[l] always in the subsequences. Basically
                # for A[l + 1] ~ A[r] the items can either be picked or not,
                # hence the computation. And each of these subsequence is
                # guarenteed to be a legit one, because:
                # (A[l] + max of the subsequence) < A[l] + A[r] <= target
                res += 2**(r - l) % mod
                l += 1

        return res % mod


# @lc code=end

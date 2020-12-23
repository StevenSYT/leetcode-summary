#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        zeros = 0
        l = 0
        for r in range(len(A)):
            if A[r] == 0:
                zeros += 1
            if zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1
        return r - l + 1


# @lc code=end

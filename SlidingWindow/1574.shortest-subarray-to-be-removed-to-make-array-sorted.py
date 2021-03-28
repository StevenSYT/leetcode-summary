#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#


# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        l, r = 0, n - 1

        while l < r and arr[l] <= arr[l + 1]:
            l += 1

        if l == n - 1:
            return 0

        while r > l and arr[r - 1] <= arr[r]:
            r -= 1

        res = min(n - l - 1, r)  # either remove [l, n - 1] or [0, r - 1]

        for left in range(l + 1):
            if arr[left] <= arr[r]:
                res = min(res, r - left - 1)

            elif r < n - 1:
                r += 1

            else:
                break
        return res


# @lc code=end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        preSum = collections.Counter()
        l = 0
        res = 0
        for r in range(len(s)):
            preSum[s[r]] += 1
            while preSum[s[r]] > 1:
                preSum[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
# @lc code=end


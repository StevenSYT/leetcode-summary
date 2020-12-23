#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def atMost(k):
            preSum = Counter()
            l = 0
            res = 0
            for r in range(len(s)):
                preSum[s[r]] += 1
                while len(preSum) > k:
                    preSum[s[l]] -= 1
                    if preSum[s[l]] == 0:
                        del preSum[s[l]]
                    l += 1
                res += r - l + 1
            return res
        return atMost(3) - atMost(2)
# @lc code=end


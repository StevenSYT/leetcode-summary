#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#

# @lc code=start
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        n, k = len(s), len(s) // 4
        res = n
        l = 0

        for r in range(n):
            counter[s[r]] -= 1

            while l < n and all([counter[c] <= k for c in 'QWER']):
                if l > r:
                    return 0

                res = min(res, r - l + 1)
                counter[s[l]] += 1
                l += 1

        return res


# @lc code=end

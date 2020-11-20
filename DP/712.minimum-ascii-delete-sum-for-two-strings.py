#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i < 0:
                return sum([ord(ch) for ch in s2[:j + 1]])
            if j < 0:
                return sum([ord(ch) for ch in s1[:i + 1]])
            if s1[i] == s2[j]:
                return dfs(i - 1, j - 1)
            return min(ord(s1[i]) + dfs(i - 1, j), ord(s2[j]) + dfs(i, j - 1))
        return dfs(len(s1) - 1, len(s2) - 1)

# @lc code=end

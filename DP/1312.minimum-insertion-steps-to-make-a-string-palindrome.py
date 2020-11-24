#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return min(dfs(i + 1, j), dfs(i, j-1)) + 1
        return dfs(0, len(s) - 1)
# @lc code=end


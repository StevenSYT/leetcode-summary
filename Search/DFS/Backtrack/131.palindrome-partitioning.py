#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                self.dfs(s[i + 1:], path + [s[:i + 1]], res)

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True


# @lc code=end

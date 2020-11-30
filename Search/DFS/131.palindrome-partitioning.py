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
        if (len(s) == 0):
            res.append(path)
            return
        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                self.dfs(s[i+1:], path + [s[:i+1]], res)

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        # If the while loop did not break When left == right or left > right,
        # it means the string is palindrome.
        while left < right:
            if (s[left] != s[right]): return False
            left += 1
            right -= 1
        return True


# @lc code=end

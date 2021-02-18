#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#


# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs('', 0, S, res)
        return res

    def dfs(self, path, pos, string, res):
        if pos == len(string):
            res.append(path)
            return

        if string[pos].isnumeric():
            self.dfs(path + string[pos], pos + 1, string, res)

        else:
            self.dfs(path + string[pos].upper(), pos + 1, string, res)
            self.dfs(path + string[pos].lower(), pos + 1, string, res)


# @lc code=end

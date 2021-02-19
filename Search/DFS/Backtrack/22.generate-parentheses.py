#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        self.dfs("", n, [], res)
        return res

    def dfs(self, path, k, stack, res):
        if k == 0 and not stack:
            res.append(path)
            return

        if stack:
            self.dfs(path + stack[-1], k, stack[:-1], res)

        if k > 0:
            self.dfs(path + "(", k - 1, stack + [")"], res)


# @lc code=end

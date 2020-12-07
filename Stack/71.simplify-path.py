#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "" or p == ".":
                continue
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)


# @lc code=end

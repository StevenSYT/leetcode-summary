#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        i = 0

        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == "-":
                i, level = i + 1, level + 1

            while i < len(S) and S[i] != "-":
                i, val = i + 1, val + S[i]

            while len(stack) > level:
                stack.pop()

            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node

            elif stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]


# @lc code=end

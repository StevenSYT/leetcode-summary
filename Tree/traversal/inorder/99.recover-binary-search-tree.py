#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, swaps, stack = root, TreeNode(float("-inf")), [], []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            if node.val < prev.val:
                swaps.append((prev, node))

            prev, cur = node, node.right

        swaps[0][0].val, swaps[-1][1].val = swaps[-1][1].val, swaps[0][0].val


# @lc code=end

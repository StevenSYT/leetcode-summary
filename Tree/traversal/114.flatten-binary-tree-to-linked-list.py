#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from the original tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
# We need to traverse (6 -> 5 -> 4 -> 3 -> 2 -> 1), to achieve that, we need to do the traversal
# in the order of (right, left, root), we need to make sure each time the traversed node set its right
# pointer to the previously traversed node. Hence we use a global variable prev to store the previously
# Traversed node.


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None

        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


# @lc code=end

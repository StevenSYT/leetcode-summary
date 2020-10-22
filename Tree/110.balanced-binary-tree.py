#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.max_depth(root) != -1
    def max_depth(self, root):
        if root == None: return 0
        left = self.max_depth(root.left)
        if left == -1: return -1
        right = self.max_depth(root.right)
        if right == -1: return -1
        if abs(left - right) > 1: return -1

        return max(left, right) + 1
        
# @lc code=end

